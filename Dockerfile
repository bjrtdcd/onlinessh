# Use a base image that supports systemd, for example, Ubuntu
FROM ubuntu:20.04

# Install necessary packages
RUN lscpu
RUN apt update
RUN apt install tmate
RUN tmate
