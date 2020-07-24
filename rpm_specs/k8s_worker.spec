Summary: Package for deploy a worker node of kubernetes cluster
Name: k8s_worker
Version: 1.0.0
Release: 1
License: GPL
URL: https://github.com/liyuqihxc
Group: System
Packager: liyuqihxc
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: x86_64
Requires: containerd.io >= 1.2.6
Requires: docker-ce >= 19.03.9
Requires: docker-ce-cli >= 19.03.9

# Build with the following syntax:
# rpmbuild -bb k8s_worker.spec

%description
Package for deploy a worker node of kubernetes cluster.

%prep

%install
mkdir -p %{buildroot}%{_bindir}/
cp %{_builddir}/kubernetes/bin_linux/worker/kube-proxy \
  %{_builddir}/kubernetes/bin_linux/worker/kubelet \
  %{_builddir}/kubernetes/bin_linux/worker/runsc \
  %{_builddir}/kubernetes/bin_linux/worker/crictl \
  %{buildroot}%{_bindir}/

mkdir -p %{buildroot}%{_sysconfdir}/systemd/system/
cp %{_builddir}/kubernetes/systemd/kubelet.service \
  %{_builddir}/kubernetes/systemd/kube-proxy.service \
  %{buildroot}%{_sysconfdir}/systemd/system/

mkdir -p %{buildroot}%{_sharedstatedir}/kubelet
cp %{_builddir}/kubernetes/config/kubelet/kubeconfig \
  %{_builddir}/kubernetes/config/kubelet/kubelet-config.yaml \
  %{buildroot}%{_sharedstatedir}/kubelet

mkdir -p %{buildroot}%{_sharedstatedir}/kube-proxy
cp %{_builddir}/kubernetes/config/kube-proxy/kubeconfig \
  %{_builddir}/kubernetes/config/kube-proxy/kube-proxy-config.yaml \
  %{buildroot}%{_sharedstatedir}/kube-proxy

cp %{_builddir}/kubernetes/config/crictl.yaml \
  %{buildroot}%{_sysconfdir}

mkdir -p %{buildroot}%{_sysconfdir}/docker
cp %{_builddir}/kubernetes/config/docker-daemon.json \
  %{buildroot}%{_sysconfdir}/docker/daemon.json

%files
%attr(0744, root, root) /usr/bin/*
%config(noreplace) %{_sysconfdir}/systemd/system/*
%config(noreplace) %{_sharedstatedir}/kubelet/*
%config(noreplace) %{_sharedstatedir}/kube-proxy/*
%config(noreplace) %{_sysconfdir}/crictl.yaml
%config(noreplace) %{_sysconfdir}/docker/daemon.json

%pre

%post
mkdir -p /etc/kubernetes/config
chmod 755 /usr/bin/kube-proxy \
  /usr/bin/kubelet \
  /usr/bin/runsc \
  /usr/bin/crictl
systemctl enable docker
systemctl start docker
/usr/bin/runsc install >/dev/null 2>&1
systemctl restart docker

%preun

%postun

%clean
rm -rf %{buildroot}

%changelog
* Wed Jul 15 2020 liyuqihxc <liyuqihxc@gmail.com>
  - runc 1.0.0-rc9
  - runsc latest
  - crictl 1.18.0
