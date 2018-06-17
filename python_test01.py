import xml.sax
import xml.sax.handler

stack = []

class Handler(xml.sax.handler.ContentHandler):
	def startElement(self, name, attrs):
		if name in ["Block", "Multi", "Thread"]:
			stack.append(attrs["id"])
			print("Start: " + name + " / id: " + attrs["id"] + "_START")
		elif name in ["Task"]:
			print("Start: " + name + " / id: " + attrs["id"])

	def endElement(self, name):
		if name in ["Block", "Multi", "Thread"]:
			print("End: " + name + " / id: " + stack.pop() + "_END")
	
	# def characters(self, content):
	# 	print("character:" + content)
	# 	return

def main():
	parser = xml.sax.make_parser()
	parser.setContentHandler(Handler())
	parser.parse("xml_test01.xml")
	return
	
if __name__=="__main__":
	main()