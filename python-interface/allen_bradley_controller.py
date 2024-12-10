from pycomm3 import LogixDriver

class ABController:
    def __init__(self, ip):
        self.plc = self.connect(ip)
        self.plc.open()
        self.plc.get_tag_list(program="AG")

    def connect(self, ip):
        return LogixDriver(ip)
    
    def get_tags(self):
        tag_list = self.plc.get_tag_list()
        output = ""
        for tag in tag_list:
            output = output+(f"Tag Name: {tag['tag_name']}\n")
        return output
    
    def print_program_tags(self, program):
        tag_list = self.plc.get_tag_list(program=program)
        output = ""
        for tag in tag_list:
            output = output+(f"Tag Name: {tag['tag_name']}\n")
        return output
    
    def get_program_tags(self, program):
        return self.plc.get_tag_list(program=program)

    def display(self):
        print(self.plc.info)
        tag_list = self.plc.get_tag_list()
        for tag in tag_list:
            print(f"Tag Name: {tag['tag_name']}, Data Type: {tag['data_type']}")

    def display_by_program(self, program):
        tag_list = self.get_program_tags(program)
        for tag in tag_list:
            print(f"Tag Name: {tag['tag_name']}, Data Type: {tag['data_type']}")

    def display_pretty(self):
        print([val[0] for val in self.plc.get_tag_list()])

    def get_value(self, value):
        return (self.plc.read(value)[1])
    

    def get_value_by_tag(self, tag):
        return (self.plc.read(tag))
    
    def set_value(self, target, value):
        self.plc.write(target, value)

    def do_this(self):
        # tag_list = self.plc.get_tag_list(program="AG")
        # for tag in tag_list:
        #     if(tag['tag_name'] == 'Program:AG.PwrProf'):
        #         print(self.plc.read(tag))

        print()
        print(self.plc.read('Program:AG.PwrProf[0]'))
        # print(self.plc.read("Program:AG.pwrProf"))





        for i in range(0,20):
            print(i)
            write_address = 'Program:AG.PwrProf[{index}]'.format(index=i)
            self.plc.write(write_address, i*20)
            # print(f'pwrProf[{i}] = {self.plc.read(write_address)}')
            
