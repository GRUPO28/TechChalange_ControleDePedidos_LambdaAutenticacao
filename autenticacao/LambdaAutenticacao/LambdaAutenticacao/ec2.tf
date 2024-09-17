data "aws_ami" "ubuntu" {
  most_recent = true
  owners = ["amazon"]
  name_regex = "Ubuntu"
}

resource "aws_instance" "web" {
  ami = data.aws_ami.ubuntu.id
  instance_type = var.instance_type
  tags = {
	Name = "${var.enviroment}: ambiente "
	Env = var.enviroment
  }
}
