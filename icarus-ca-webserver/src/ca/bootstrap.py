import inspect
import logging
from . import config


from .service_layer import messagebus, handlers, unit_of_work as uow

LOG_FORMAT = "%(asctime)s %(message)s"
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)


def bootstrap(start_orm: bool = True, unit_of_work=uow.SqlAlchemyUnitOfWork()):

    dependencies = {"uow": unit_of_work}

    injected_event_handlers = {
        event_type: [
            inject_dependencies(handler, dependencies) for handler in event_handlers
        ]
        for event_type, event_handlers in handlers.EVENT_HANDLERS.items()
    }

    injected_command_handlers = {
        command_type: inject_dependencies(handler, dependencies)
        for command_type, handler in handlers.COMMAND_HANDLERS.items()
    }

    return messagebus.MessageBus(
        command_handlers=injected_command_handlers,
        event_handlers=injected_event_handlers,
        uow=unit_of_work,
    )


def inject_dependencies(handler, dependencies):
    params = inspect.signature(handler).parameters

    deps = {
        name: dependency for name, dependency in dependencies.items() if name in params
    }
    return lambda message: handler(message, **deps)
