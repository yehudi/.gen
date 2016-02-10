import sys
import os
import json

directory = os.path.dirname(os.path.realpath(__file__))

site = {}
site['url'] = input("Site url ?")
site['title'] = site["url"]
site['version'] = "1.0.0"
site['last-update'] = ""
site['locales'] = []
locale = "0"

print("Add the website languages (iso, ex: fr for french)")
print("press Enter to finish")

while len(locale) > 0:
	locale=input("\tAdd a language : ")
	if len(locale) > 0:
		site['locales'].append(locale)

site["locales_names"] = site["locales"]

if len(site["locales"])>0:
	site["default_locale"] = site["locales"][0]
else:
	site["default_locale"] = ""

with open("conf/site.json","w") as f:
	f.write(json.dumps(site,sort_keys=True,indent=4, separators=(',', ': ')))
	f.close()

pages = {}
pages["home"] = {"default" : True, "menu" : True}
pages["contact"] = {"menu" : True}

with open("conf/pages.json","w") as f:
	f.write(json.dumps(pages,sort_keys=True,indent=4, separators=(',', ': ')))

for e in site["locales"]:
	with open("conf/locales/"+e+".json", "w") as f:
		locales = {"pages" : {}, "data" : {}}
		for p in pages:
			locales["pages"][p] = {"title" : "Page title", "content" : []}
		f.write(json.dumps(locales,sort_keys=True,indent=4, separators=(',', ': ')))
		f.close()

with open(directory+'/default_package.json') as f:    
    data = json.load(f)
    with open("package.json", "w") as fi:
    	data["name"] = site["url"]
    	fi.write(json.dumps(data,sort_keys=True,indent=4, separators=(',', ': ')))
    	fi.close()
    f.close()
