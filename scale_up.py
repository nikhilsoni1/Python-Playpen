import repository_scraper as rs
url = "https://ag.purdue.edu/scaleup/Presentation%20Library/Forms/AllItems.aspx"
url1 = "https://ag.purdue.edu/scaleup/Presentation%20Library/Forms/AllItems.aspx#InplviewHash825b1321-473c-49a8-ac17-339a6501cc13=Paged%3DTRUE-p_SortBehavior%3D0-p_FileLeafRef%3DRunnalls%252dSession%25203%2520Part%2520Il%2520%252d%2520Finance%2520Overview%252epdf-p_ID%3D6-PageFirstRow%3D31"
find = ("table", {"id": "onetidDoclibViewTbl0"})
findall = "a"
corpus = rs.Repository(url1, find, findall)
root = "https://ag.purdue.edu"
print(corpus.data)
# for i in corpus.data:
#     target = i.find("a")
#     if target:
#         pdf_url = root+target["href"]
#         pdf_url = pdf_url.replace(" ", "%20")
#         pdf_data = rs.url_response(pdf_url)
#         pdf_name = target.text+".pdf"
#         destination = "output/scale_up/"+pdf_name
#         with open(destination, "wb") as pdf:
#             pdf.write(pdf_data.data)
