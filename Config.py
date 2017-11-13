# Relative path of pattern file to GitPrey
FILE_DB = "pattern/file.db"
INFO_DB = "pattern/info.db"

# GitHub account config for searching
USER_NAME = ""
PASSWORD = ""

# Blacklist
EXT_BLACKLIST = [".ico", ".flv", ".css", ".jpg", ".png", ".jpeg", ".gif", ".pdf", ".ss3", ".rar", ".zip", ".avi", ".mp4", ".swf", ".wmi", ".exe", ".mpeg", ".dll", ".pcap", ".log", ".class", ".html"]
LANG_BLACKLIST = ["html", "jsp", "smali"]
LINE_MUSTHAVE = ['=', ':', 'define']
REPO_NAME_BLACKLIST = ['spider', 'crawl']

# other
MAX_INFONUM = 3
MAX_LINELEN = 512
MAX_COUNT_SINGLE_FILE = 20
MAX_SEARCH_REPO = 20
MAX_REPO_SINGLE_SEARCH = 5