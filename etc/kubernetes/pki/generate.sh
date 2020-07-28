#！/usr/bin/env bash

set -e

cfssl gencert -initca ca-csr.json | cfssljson -bare ca

CA_CER=../ca.pem
CA_KEY=../ca-key.pem
CA_CFG=../ca-config.json

cfssl gencert \
  -ca=$CA_CER \
  -ca-key=$CA_KEY \
  -config=$CA_CFG \
  -profile=kubernetes \
  admin-csr.json | cfssljson -bare admin

cfssl gencert \
  -ca=$CA_CER \
  -ca-key=$CA_KEY \
  -config=$CA_CFG \
  -profile=kubernetes \
  kube-controller-manager-csr.json | cfssljson -bare kube-controller-manager

cfssl gencert \
  -ca=$CA_CER \
  -ca-key=$CA_KEY \
  -config=$CA_CFG \
  -profile=kubernetes \
  kube-proxy-csr.json | cfssljson -bare kube-proxy

cfssl gencert \
  -ca=$CA_CER \
  -ca-key=$CA_KEY \
  -config=$CA_CFG \
  -profile=kubernetes \
  kube-scheduler-csr.json | cfssljson -bare kube-scheduler

cfssl gencert \
  -ca=$CA_CER \
  -ca-key=$CA_KEY \
  -config=$CA_CFG \
  -hostname=192.168.56.100,192.168.56.101,192.168.56.102,127.0.0.1,kubernetes.default \
  -profile=kubernetes \
  kubernetes-csr.json | cfssljson -bare kubernetes

cfssl gencert \
  -ca=$CA_CER \
  -ca-key=$CA_KEY \
  -config=$CA_CFG \
  -profile=kubernetes \
  service-account-csr.json | cfssljson -bare service-account
