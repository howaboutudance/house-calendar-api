#!/bin/bash
set +e

#Checks if network exists
#TODO: #7 parameterize network name
if [ "$(podman network exists house-calendar-backend)" == "1" ] ; then
  podman network create house-calendar-backend
fi

#TODO: Parameterize yaml file name for podman yaml defitnition
#TODO: Investigate: pod setup with shell script
if [ "$(podman pod ps |grep -E "api_pod|phppgadmin_pod|db" | wc -l)" == "0" ] ; then
  echo "> > > Starting PostgreSQL, house_calendar and phppgadmin"
  podman play kube --network=house-calendar-backend scripts/pods/backend.yaml
else
  echo "Development pod is already running. Re-create it? Y/N"
  read input
  # TODO: Fix to hand yes and y cass
  if [ $input == "Y" ] ; then
    podman pod rm api_pod -f
    podman pod rm phppgadmin_pod -f
    podman pod rm db -f
    podman play kube --network=house-calendar-backend scripts/pods/backend.yaml
  else
    echo "Leaving bootstrap process."
    exit 0
  fi
fi