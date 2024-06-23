# Use a base image that supports systemd, for example, Ubuntu
FROM ubuntu:20.04

# Update package lists and install tmate
RUN apt-get update && \
    apt-get install -y tmate && \
    rm -rf /var/lib/apt/lists/*

# Start tmate when the container starts
CMD ["tmate"]
