import xml.sax
import xml.sax.handler

stack = []

class Handler(xml.sax.handler.ContentHandler):
	def startElement(self, name, attrs):
		stack.append(attrs["id"])
		print("Start: " + name + " / id: " + attrs["id"] + "_START")

	def endElement(self, name):
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