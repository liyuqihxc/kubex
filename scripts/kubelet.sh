#!/usr/bin/env bash

/usr/bin/kubelet \
  --bootstrap-kubeconfig=/etc/kubernetes/bootstrap-kubelet.conf \
  --kubeconfig=/etc/kubernetes/kubelet.conf \
  --config=/var/lib/kubelet/config.yaml \
  --cgroup-driver=systemd \
  --network-plugin=cni \
  --pod-infra-container-image=k8s.gcr.io/pause:3.2
