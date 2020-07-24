# https://fedoraproject.org/wiki/How_to_create_an_RPM_package/zh-cn#.E5.85.B6.E5.AE.83.E6.A0.87.E7.AD.BE
# https://jin-yang.github.io/post/linux-create-rpm-package.html
# https://ro-che.info/articles/2018-01-25-rpm-packager-cheat-sheet
Summary: Package for deploy a master node of kubernetes HA cluster
Name: k8s_master
Version: 1.0.0
Release: 1
License: GPL
URL: https://github.com/liyuqihxc
Group: System
# Source: kubernetes-master.tar.gz
Packager: liyuqihxc
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: x86_64

# Build with the following syntax:
# rpmbuild -bb k8s_master.spec

%description
Package for deploy a master node of kubernetes HA cluster.

%prep

%install
mkdir -p %{buildroot}%{_bindir}/
cp %{_builddir}/kubernetes/bin_linux/master/etcd \
  %{_builddir}/kubernetes/bin_linux/master/etcdctl \
  %{_builddir}/kubernetes/bin_linux/master/kube-apiserver \
  %{_builddir}/kubernetes/bin_linux/master/kube-controller-manager \
  %{_builddir}/kubernetes/bin_linux/master/kube-scheduler \
  %{_builddir}/kubernetes/bin_linux/master/kubectl \
  %{buildroot}%{_bindir}/

mkdir -p %{buildroot}%{_sysconfdir}/systemd/system/
cp %{_builddir}/kubernetes/systemd/etcd.service \
  %{_builddir}/kubernetes/systemd/kube-apiserver.service \
  %{_builddir}/kubernetes/systemd/kube-controller-manager.service \
  %{_builddir}/kubernetes/systemd/kube-scheduler.service \
  %{buildroot}%{_sysconfdir}/systemd/system/

mkdir -p %{buildroot}%{_sysconfdir}/kubernetes/config/env
cp %{_builddir}/kubernetes/config/env/etcd \
  %{_builddir}/kubernetes/config/env/kube-apiserver \
  %{_builddir}/kubernetes/config/env/kube-controller-manager \
  %{buildroot}%{_sysconfdir}/kubernetes/config/env/

mkdir -p %{buildroot}%{_sysconfdir}/kubernetes/config
cp %{_builddir}/kubernetes/config/encryption-config.yaml \
  %{_builddir}/kubernetes/config/kube-controller-manager.kubeconfig \
  %{_builddir}/kubernetes/config/kube-scheduler.kubeconfig \
  %{_builddir}/kubernetes/config/kube-scheduler.yaml \
  %{buildroot}%{_sysconfdir}/kubernetes/config/

%files
%attr(0744, root, root) /usr/bin/*
%config(noreplace) %{_sysconfdir}/systemd/system/*
%config(noreplace) %{_sysconfdir}/kubernetes/config/*

%pre

%post
chmod 755 /usr/bin/etcd \
  /usr/bin/etcdctl \
  /usr/bin/kube-apiserver \
  /usr/bin/kube-controller-manager \
  /usr/bin/kube-scheduler \
  /usr/bin/kubectl

%preun

%postun

%clean
rm -rf %{buildroot}

%changelog
* Wed Jul 15 2020 liyuqihxc <liyuqihxc@gmail.com>
  - kubernetes 1.18.5
  - etcd 3.4.9
