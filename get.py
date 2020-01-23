from youtube_transcript_api import YouTubeTranscriptApi

vids = ["2hVL9r1vy8I",
"_uE_CAnzkok",
"Jd1ZdgWT3jA",
"4TBwiLTesFs",
"ScNBYXaGKeY",
"30YyUAI8IZM",
"2NROe-Sm8Gk",
"OmGoZEbT6eM",
"pNOj4rDNRvg",
"eIHz2APDGuQ",
"nuXJjDkawDU",
"9PoE1a0sjcg",
"JKaZYONagi0",
"E-njMDdhjA8",
"LoywF8tzM_c",
"QeC_zQLMliQ",
"RXGEJUIbalA",
"JTYdDUXjJ3Q",
"wa9Whoe6P6k",
"61gUDUv7X24",
"ClMcM6drltc",
"7b5cbaafql8",
"ZBr-m-EwIoQ",
"zkkP60QQX7c"]

data = []
for video_id in vids:
    temp = YouTubeTranscriptApi.get_transcript(video_id)
    data.append([x["text"] for x in temp])

with open("gg.txt","w") as file:
    for xx in data:
        for yy in xx:
            file.write(yy+"\n")