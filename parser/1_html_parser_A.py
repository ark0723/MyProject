from html.parser import HTMLParser

import codecs
f=codecs.open("snu_labs.html", 'r',encoding="UTF-8")
data = f.read()
# print (data)

class AllLanguages(HTMLParser):

    def __init__(self):
        HTMLParser.__init__(self)
        self.titleArray = []
        self.nameArray = []
        self.phoneArray = []
        self.officeArray = []
        self.labArray = []
        self.diction={}

        self.lasttag = None
        self.inLink=True
        self.name=None
        self.value=None

    def handle_starttag(self, tag, attr):
        if tag == 'td':
            for name, value in attr:
                self.name = name
                self.value = value

    def handle_data(self, data):
        if self.value == "views-field views-field-title" and data.strip() and (self.lasttag == 'a'):
            self.titleArray.append(data.rstrip())

        if self.value == "views-field views-field-field-faculty"  and  data.strip() and (self.lasttag == 'a') and (data!=', ') :
            self.nameArray.append(data)

        if (self.lasttag == 'br') and self.inLink and data.strip():
            self.phoneArray.append(data.rstrip())

        if (self.lasttag == 'td') and self.value == "views-field views-field-field-office"  and self.inLink and data.split('/') and data.strip():

            self.officeArray.append(data.rstrip().lstrip())


        if (self.lasttag == 'td') and self.value == "views-field views-field-field-abbreviation"  and self.inLink and data.strip():
            self.labArray.append(data.rstrip().lstrip())

    def make_diction(self):
        self.diction['title'] = self.titleArray
        self.diction['professor']=self.nameArray
        self.diction['phone']=self.phoneArray
        self.diction['location']=self.officeArray
        self.diction['abbreviation'] = self.labArray

        return self.diction


parser = AllLanguages()
parser.feed(data)
print(parser.make_diction())
