def error(*args, **kwargs):
    print("\033[91m[ERROR  ] " + " ".join(map(str, args))+"\033[0m", **kwargs)

def warning(*args, **kwargs):
    print("\033[93m[WARNING] " + " ".join(map(str, args))+"\033[0m", **kwargs)

def note(*args, **kwargs):
    print("\033[90m[NOTE   ] " + " ".join(map(str, args))+"\033[0m", **kwargs)

def info(*args, **kwargs):
    print("\033[95m[INFO   ] " + " ".join(map(str, args))+"\033[0m", **kwargs)
