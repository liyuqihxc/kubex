#!/usr/bin/env bash

CLUSTER_NAME=kubex
CLUSTER_ENDPOINT=127.0.0.1:6443
CERTS=/etc/kubernetes/pki
NODE_NAME=kubex-master1

# admin.conf
kubectl config set-cluster $CLUSTER_NAME \
  --certificate-authority=$CERTS/ca.pem \
  --embed-certs=true \
  --server=https://$CLUSTER_ENDPOINT \
  --kubeconfig=admin.conf

kubectl config set-credentials admin \
  --client-certificate=$CERTS/admin.pem \
  --client-key=$CERTS/admin.pem \
  --embed-certs=true \
  --kubeconfig=admin.conf

kubectl config set-context admin@$CLUSTER_NAME \
  --cluster=$CLUSTER_NAME \
  --user=admin \
  --kubeconfig=admin.conf

kubectl config use-context admin@$CLUSTER_NAME --kubeconfig=admin.conf

# kube-controller-manager.conf
kubectl config set-cluster $CLUSTER_NAME \
  --certificate-authority=$CERTS/ca.pem \
  --embed-certs=true \
  --server=https://$CLUSTER_ENDPOINT \
  --kubeconfig=kube-controller-manager.conf

kubectl config set-credentials system:kube-controller-manager \
  --client-certificate=$CERTS/kube-controller-manager.pem \
  --client-key=$CERTS/kube-controller-manager-key.pem \
  --embed-certs=true \
  --kubeconfig=kube-controller-manager.conf

kubectl config set-context system:kube-controller-manager@$CLUSTER_NAME \
  --cluster=$CLUSTER_NAME \
  --user=system:kube-controller-manager \
  --kubeconfig=kube-controller-manager.conf

kubectl config use-context system:kube-controller-manager@$CLUSTER_NAME --kubeconfig=kube-controller-manager.conf

# kube-scheduler.conf
kubectl config set-cluster $CLUSTER_NAME \
  --certificate-authority=$CERTS/ca.pem \
  --embed-certs=true \
  --server=https://$CLUSTER_ENDPOINT \
  --kubeconfig=kube-scheduler.conf

kubectl config set-credentials system:kube-scheduler \
  --client-certificate=$CERTS/kube-scheduler.pem \
  --client-key=$CERTS/kube-scheduler-key.pem \
  --embed-certs=true \
  --kubeconfig=kube-scheduler.conf

kubectl config set-context system:kube-scheduler@$CLUSTER_NAME \
  --cluster=$CLUSTER_NAME \
  --user=system:kube-scheduler \
  --kubeconfig=kube-scheduler.conf

kubectl config use-context system:kube-scheduler@$CLUSTER_NAME --kubeconfig=kube-scheduler.conf

# kubelet.conf
kubectl config set-cluster $CLUSTER_NAME \
  --certificate-authority=$CERTS/ca.pem \
  --embed-certs=true \
  --server=https://$CLUSTER_ENDPOINT \
  --kubeconfig=kubelet.conf

kubectl config set-credentials system:node:$NODE_NAME \
  --client-certificate=/var/lib/kubelet/pki/kubelet-client-current.pem \
  --client-key=/var/lib/kubelet/pki/kubelet-client-current.pem \
  --kubeconfig=kubelet.conf

kubectl config set-context system:node:$NODE_NAME@$CLUSTER_NAME \
  --cluster=$CLUSTER_NAME \
  --user=system:node:$NODE_NAME \
  --kubeconfig=kubelet.conf

kubectl config use-context system:node:$NODE_NAME@$CLUSTER_NAME --kubeconfig=kubelet.conf
