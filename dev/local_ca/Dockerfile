FROM ubuntu:18.04

RUN apt update && apt install -y apache2-utils git openssl libssl-dev build-essential && \
    git clone https://github.com/cisco/libest.git && cd libest && \
    ./configure --disable-safec && make install && \
    rm -rf /src && apt remove --quiet -y libssl-dev build-essential && \
    apt autoremove -y && apt clean -y && apt autoclean -y && \
    rm -rf /var/lib/apt /tmp/* /var/tmp/*

WORKDIR /libest/example/server/

# Setting the root CA expiration to 20 years
RUN sed -i "s|-days 365|-days 7300 |g" ./createCA.sh

## If you want to host your EST server in the cloud (for example, an Azure Container Instance),
## change myestserver.westus.azurecontainer.io to the fully qualified DNS name of your EST server 
## and uncomment the next line.
# RUN sed -i "s|ip6-localhost|myestserver.westus.azurecontainer.io |g" ./ext.cnf

# Set EST server certificate to be valid for 10 years
RUN sed -i "s|-keyout \$EST_SERVER_PRIVKEY -subj|-keyout \$EST_SERVER_PRIVKEY -days 7300 -subj |g" ./createCA.sh

# Create the CA
RUN echo 1 | ./createCA.sh

# Set cert default-days to 1 to show EST renewal
RUN sed -i "s|default_days   = 365|default_days   = 1 |g" ./estExampleCA.cnf

# The EST server listens on port 8085 by default
# Uncomment to change the port to 443 or something else. If changed, EXPOSE that port instead of 8085. 
# RUN sed -i "s|estserver -c|estserver -p 443 -c |g" ./runserver.sh
EXPOSE 8085
CMD ./runserver.sh