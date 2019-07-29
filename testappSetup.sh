#!/usr/bin/env bash
#sudo chmod 777 testappSetup.sh
#sudo ./testappSetup.sh

install_app(){
	git clone https://github.com/nguyendinhhh/integration-testing.git --branch installBranch
	cd integration-testing
	fbs freeze
	fbs installer
	sudo dpkg -i target/testapp.deb
}


main () {
	
	install_app
	
}

main "$@"
