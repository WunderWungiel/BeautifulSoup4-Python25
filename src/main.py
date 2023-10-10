from dedomil import get_resolutions, get_app_info, search, retrieve_games
import random
import subprocess
import os

results = search("Asphalt").results

print results

random_game = list(results.values())[random.randint(1, 9)]['link']

resolutions = get_resolutions(random_game)
print resolutions

random_res = list(resolutions.values())[0]

app_info = get_app_info("http://dedomil.net/games/263/screen/8")

print "Title:", app_info.title, "\n"
print "Splash:", app_info.splash, "\n"
print "Screenshots:", app_info.screenshots, "\n"
print "Date:", app_info.date, "\n"
print "Counter:", app_info.counter, "\n"
print "Vendor:", app_info.vendor, "\n"
print "Description:", "\n", app_info.description, "\n"

print app_info.download_links