vms=5

Vagrant.configure("2") do |config|
  (1..vms).each do |i|
    port=8080+i
    config.vm.define "node-#{i}" do |node|
      node.vm.box = "ubuntu/trusty64"
      node.vm.network "forwarded_port", guest: 80, host: port
      node.vm.provision :ansible do |ansible|
        ansible.playbook = "webserver.yml"
        ansible.extra_vars = {node_id: i }
      end
    end
  end

  config.vm.define "balancer" do |node|
    node.vm.box = "ubuntu/trusty64"
    node.vm.network "forwarded_port", guest: 80, host: 80
    node.vm.provision :ansible do |ansible|
      ansible.playbook = "balancer.yml"
      ansible.extra_vars = {nodes: vms }
    end
    node.vm.provision "shell", path: "nodes.sh", args: vms
  end
end
