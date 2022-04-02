Vagrant.configure(2) do |config|

    config.vm.define "backend" do |backend|

        backend.vm.box = "archlinux/archlinux"

        backend.vm.provider "virtualbox" do |vb|
            vb.memory = "1024"
            vb.customize [ "modifyvm", :id, "--vram", "16" ]
            vb.customize [ "modifyvm", :id, "--uart1", "off" ]
            vb.customize [ "modifyvm", :id, "--uart2", "off" ]
            vb.customize [ "modifyvm", :id, "--uart3", "off" ]
            vb.customize [ "modifyvm", :id, "--uart4", "off" ]
        end

        # port forwarding
        backend.vm.network "forwarded_port", guest: 8000, host: 8000

        # use Ansible from host (or WSL in case of Windows)
        backend.ssh.insert_key = false
        backend.ssh.private_key_path = "~/.vagrant.d/insecure_private_key"

        backend.vm.provision "ansible" do |ansible|
            ansible.playbook = "playbook.yml"
        end
    end
end
