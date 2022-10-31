"""create init tables

Revision ID: ae929aae2d76
Revises: 
Create Date: 2022-07-26 09:46:17.937505

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "ae929aae2d76"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "leaf_certificate_signing_requests",
        sa.Column("uid", sa.String(100), primary_key=True),
        sa.Column("cn", sa.String(100), nullable=False),
        sa.Column("csr", sa.Text, nullable=False),
    )


def downgrade():
    pass
