import json

# Rock Paper Scissors

def rpsDataSave(user, bot, winner):
    with open("Saves/rps.json", "r") as f:
        data = json.load(f)

    data["count"] += 1
    winned = data["count"]

    data["games"][f"game {winned}"] = {
        "user": user,
        "bot": bot,
        "win": winner
    }

    data["dataAnalysis"]["user"] += [user]
    data["dataAnalysis"]["bot"] += [bot]
    data["dataAnalysis"]["winner"] += [winner]

    with open("Saves/rps.json", "w") as f:
        json.dump(data, f, indent=4)

    rpsDataAnalyse()

def rpsDataAnalyse():
    with open("Saves/rps.json", "r") as f:
        data = json.load(f)

    userActions = {
        "rock": data["dataAnalysis"]["user"].count("Rock"),
        "paper": data["dataAnalysis"]["user"].count("Paper"),
        "scissors": data["dataAnalysis"]["user"].count("Scissors"),
        "total": len(data["dataAnalysis"]["user"])
    }

    prc = {
        "Rock": (userActions["rock"] * 100) / userActions["total"],
        "Paper": (userActions["paper"] * 100) / userActions["total"],
        "Scissors": (userActions["scissors"] * 100) / userActions["total"]
    }

    data["dataAnalysis"]["prc"] = prc

    with open("Saves/rps.json", "w") as f:
        json.dump(data, f, indent=4)

def rpsDataActions():
    with open("Saves/rps.json", "r") as f:
        data = json.load(f)

    if data["dataAnalysis"]["prc"]["Rock"] > data["dataAnalysis"]["prc"]["Paper"] and data["dataAnalysis"]["prc"]["Rock"] > data["dataAnalysis"]["prc"]["Scissors"]:
        return "Rock"
    if data["dataAnalysis"]["prc"]["Paper"] > data["dataAnalysis"]["prc"]["Rock"] and data["dataAnalysis"]["prc"]["Paper"] > data["dataAnalysis"]["prc"]["Scissors"]:
        return "Paper"
    if data["dataAnalysis"]["prc"]["Scissors"] > data["dataAnalysis"]["prc"]["Paper"] and data["dataAnalysis"]["prc"]["Scissors"] > data["dataAnalysis"]["prc"]["Rock"]:
        return "Scissors"

# Quiz

def quizDataSave(q1):
    with open("Saves/quiz.json", "r") as f:
        data = json.load(f)

    data["count"] += 1
    count = data["count"]

    data["saves"][f"awnsers {count}"] = {
        "Q1": q1
    }

    for i in range(1, 11):
        if q1 == i:
            data["data"]["Q1"][f"{i}"] += 1

    data["data"]["Q1"]["total"] += 1

    with open("Saves/quiz.json", "w") as f:
        json.dump(data, f, indent=4)

    quizDataAnalyse()

def quizDataAnalyse():
    with open("Saves/quiz.json", "r") as f:
        data = json.load(f)

    data["prc"]["Q1"] = {
        "1": prc(data["data"]["Q1"]["1"], data["data"]["Q1"]["total"]),
        "2": prc(data["data"]["Q1"]["2"], data["data"]["Q1"]["total"]),
        "3": prc(data["data"]["Q1"]["3"], data["data"]["Q1"]["total"]),
        "4": prc(data["data"]["Q1"]["4"], data["data"]["Q1"]["total"]),
        "5": prc(data["data"]["Q1"]["5"], data["data"]["Q1"]["total"]),
        "6": prc(data["data"]["Q1"]["6"], data["data"]["Q1"]["total"]),
        "7": prc(data["data"]["Q1"]["8"], data["data"]["Q1"]["total"]),
        "9": prc(data["data"]["Q1"]["9"], data["data"]["Q1"]["total"]),
        "10": prc(data["data"]["Q1"]["10"], data["data"]["Q1"]["total"])
    }

    with open("Saves/quiz.json", "w") as f:
        json.dump(data, f, indent=4)

# Others

def prc(num, total):
    prc = (num * 100) / total
    return prc

def reset(target):
    if target == "quiz":
        with open("Saves/quiz.json", "r") as f:
            data = json.load(f)

        data["count"] = 0

        for i in range(1, 11):
            data["data"]["Q1"][f"{i}"] = 0
            data["prc"]["Q1"][f"{i}"] = 0.0

        data["data"]["Q1"]["total"] = 0
        data["saves"] = {}

        with open("Saves/quiz.json", "w") as f:
            json.dump(data, f, indent=4)

    elif target == "rps":
        with open("Saves/rps.json", "r") as f:
            datarps = json.load(f)

        datarps["count"] = 0

        datarps["dataAnalysis"]["bot"] = []
        datarps["dataAnalysis"]["user"] = []
        datarps["dataAnalysis"]["winner"] = []

        datarps["dataAnalysis"]["prc"]["Rock"] = 0.0
        datarps["dataAnalysis"]["prc"]["Paper"] = 0.0
        datarps["dataAnalysis"]["prc"]["Scissors"] = 0.0

        datarps["games"] = {}

        with open("Saves/rps.json", "w") as f:
            json.dump(datarps, f, indent=4)
    else:
        "Error: Target have to be either quiz or rps"


