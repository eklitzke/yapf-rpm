srpm:
	dnf -y install rpmdevtools fedpkg
	spectool -g python-yapf.spec
	fedpkg --release=f27 srpm
	cp *.src.rpm $(outdir)
