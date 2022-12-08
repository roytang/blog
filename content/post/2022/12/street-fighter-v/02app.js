let characterList = [];
let characterMap = {};
let platforms = ["Both", "Steam", "PS4"];

for (let i = 0; i < characterData.length; i++) {
    let character = characterData[i]["character"];
    let platform = characterData[i]["platform"];
    if (character in characterMap) {
        characterMap[character][platform] = characterData[i];
    } else {
        characterMap[character] = {}
        characterMap[character][platform] = characterData[i];
    }
    let matchups = characterData[i]["matchups"];
    for (let j = 0; j < matchups.length; j++) {
        let characterName = matchups[j]["vs"];
        if (characterList.indexOf(characterName) < 0) {
            characterList.push(characterName);
        }
    }
}

let overall = {
    "Both": {
        "character": "Overall",
        "platform": "Both",
        "totalMatches": 0,
        "overallWinrate": 0,
        "wins": 0, // temp variable needed for accumulating totals
        "matchups": [],
        "matchupsMap": {}
    },
    "Steam": {
        "character": "Overall",
        "platform": "Steam",
        "totalMatches": 0,
        "overallWinrate": 0,
        "wins": 0, // temp variable needed for accumulating totals
        "matchups": [],
        "matchupsMap": {}
    },
    "PS4": {
        "character": "Overall",
        "platform": "PS4",
        "totalMatches": 0,
        "overallWinrate": 0,
        "wins": 0, // temp variable needed for accumulating totals
        "matchups": [],
        "matchupsMap": {}
    },
}

let overallCharacterMap = {
    "Both": [],
    "Steam": [],
    "PS4": [],
}
let characterSelect = document.querySelector("#character");
let playedChars = Object.keys(characterMap);
for (let i = 0; i < playedChars.length; i++) {
    // populate select controls
    let option = document.createElement("option");
    option.innerText = playedChars[i];
    option.value = playedChars[i];
    characterSelect.appendChild(option);

    // populate "Both" platform
    let selectedCharacterMap = characterMap[playedChars[i]];
    if ("Steam" in selectedCharacterMap && "PS4" in selectedCharacterMap) {
        let steam = selectedCharacterMap["Steam"];
        let ps4 = selectedCharacterMap["PS4"];
        let totalMatches = steam["totalMatches"] + ps4["totalMatches"];
        let wins = Math.round(steam["totalMatches"] * steam["overallWinrate"]) + Math.round(ps4["totalMatches"] * ps4["overallWinrate"]);
        let winrate = Math.round(10000*wins/totalMatches)/10000;
        // merge the matchups data
        let matchupsMap = {}
        let sourceMatchups = [ps4["matchups"], steam["matchups"]];
        for (let k = 0; k < sourceMatchups.length; k++) {
            let fromMatchups = sourceMatchups[k];
            for (let j = 0; j < fromMatchups.length; j++) {
                let matchup = fromMatchups[j];
                let vsName = matchup["vs"];
                if (vsName in matchupsMap) {
                    let newTotalMatches = matchupsMap[vsName]["matches"] + matchup["matches"];
                    let newWins = Math.round(matchupsMap[vsName]["matches"] * matchupsMap[vsName]["winrate"]) + Math.round(matchup["matches"] * matchup["winrate"]);
                    let winrate = Math.round(10000*newWins/newTotalMatches)/10000;
                    matchupsMap[vsName] = {
                        "vs": vsName,
                        "matches": newTotalMatches,
                        "winrate": winrate
                    }
                } else {
                    matchupsMap[vsName] = {
                        "vs": vsName,
                        "matches": matchup["matches"],
                        "winrate": matchup["winrate"]
                    }
                }
            }
        }
        let matchupsKeys = Object.keys(matchupsMap);
        let newMatchups = [];
        for (let j = 0; j < matchupsKeys.length; j++) {
            newMatchups.push(matchupsMap[matchupsKeys[j]]);
        }
        let newObject = {
            "character": playedChars[i],
            "platform": "Both",
            "totalMatches": totalMatches,
            "overallWinrate": winrate,
            "matchups": newMatchups
        }
        selectedCharacterMap["Both"] = newObject;
        overallCharacterMap["Both"].push({
            "character": playedChars[i],
            "matches": totalMatches,
            "winrate": winrate,
        });
        overallCharacterMap["Steam"].push({
            "character": playedChars[i],
            "matches": selectedCharacterMap["Steam"]["totalMatches"],
            "winrate": selectedCharacterMap["Steam"]["overallWinrate"],
        });
        overallCharacterMap["PS4"].push({
            "character": playedChars[i],
            "matches": selectedCharacterMap["PS4"]["totalMatches"],
            "winrate": selectedCharacterMap["PS4"]["overallWinrate"],
        });
    } else if ("Steam" in selectedCharacterMap) {
        selectedCharacterMap["Both"] = selectedCharacterMap["Steam"]
        let overallData = {
            "character": playedChars[i],
            "matches": selectedCharacterMap["Steam"]["totalMatches"],
            "winrate": selectedCharacterMap["Steam"]["overallWinrate"],
        }
        overallCharacterMap["Both"].push(overallData);
        overallCharacterMap["Steam"].push(overallData);
    } else if ("PS4" in selectedCharacterMap) {
        selectedCharacterMap["Both"] = selectedCharacterMap["PS4"]
        let overallData = {
            "character": playedChars[i],
            "matches": selectedCharacterMap["PS4"]["totalMatches"],
            "winrate": selectedCharacterMap["PS4"]["overallWinrate"],
        }
        overallCharacterMap["Both"].push(overallData);
        overallCharacterMap["PS4"].push(overallData);
    }
    
    // populate "Overall" character profile
    for (let j = 0; j < platforms.length; j++) {
        let platform = platforms[j];
        if (platform in selectedCharacterMap) {
            let thisData = selectedCharacterMap[platform];
            overall[platform]["totalMatches"] = overall[platform]["totalMatches"] + thisData["totalMatches"];
            let wins = Math.round(thisData["totalMatches"] * thisData["overallWinrate"]);
            overall[platform]["wins"] = overall[platform]["wins"] + wins;

            let matchupsMap = overall[platform]["matchupsMap"];
            for (let k = 0; k < thisData["matchups"].length; k++) {
                let matchup = thisData["matchups"][k];
                let vsName = matchup["vs"];
                if (vsName in matchupsMap) {
                    let newTotalMatches = matchupsMap[vsName]["matches"] + matchup["matches"];
                    let newWins = Math.round(matchupsMap[vsName]["matches"] * matchupsMap[vsName]["winrate"]) + Math.round(matchup["matches"] * matchup["winrate"]);
                    let winrate = Math.round(10000*newWins/newTotalMatches)/10000;
                    matchupsMap[vsName] = {
                        "vs": vsName,
                        "matches": newTotalMatches,
                        "winrate": winrate
                    }
                } else {
                    matchupsMap[vsName] = {
                        "vs": vsName,
                        "matches": matchup["matches"],
                        "winrate": matchup["winrate"]
                    }
                }
            }
            overall[platform]["matchupsMap"] = matchupsMap;
        }
    }
    characterMap[playedChars[i]] = selectedCharacterMap;
}
// final "Overall" computations
for (let j = 0; j < platforms.length; j++) {
    let platform = platforms[j];
    overall[platform]["overallWinrate"] = Math.round(10000 * overall[platform]["wins"] / overall[platform]["totalMatches"]) / 10000;

    let matchupsKeys = Object.keys(overall[platform]["matchupsMap"]);
    for (let j = 0; j < matchupsKeys.length; j++) {
        overall[platform]["matchups"].push(overall[platform]["matchupsMap"][matchupsKeys[j]]);
    }

}
characterMap["Overall"] = overall;
console.log(overall);

function createCell(contents) {
    let newCell = document.createElement("td");
    newCell.innerText = contents;
    return newCell;
}
function renderData() {
    let selectedCharacter = document.querySelector("#character").value;
    let selectedPlatform = document.querySelector("#platform").value;
    let tbody = document.querySelector("tbody.played_data");
    tbody.innerHTML = "";
    let playedHeader = document.querySelector("thead.played_header");
    playedHeader.style.display = "none";
    if (selectedCharacter == "Overall") {
        playedHeader.style.display = "table-header-group";
        let platformCharacters = overallCharacterMap[selectedPlatform];
        platformCharacters.sort((a, b) => {
            return b["matches"] - a["matches"];
        });
        tbody.innerHTML = "";
        for (let i = 0; i < platformCharacters.length; i++) {
            let newRow = document.createElement("tr");
            let charName = platformCharacters[i]["character"];
            newRow.appendChild(createCell(charName));
            newRow.appendChild(createCell(platformCharacters[i]["matches"]));
            newRow.appendChild(createCell(platformCharacters[i]["winrate"]));
            let wins = Math.round(platformCharacters[i]["matches"] * platformCharacters[i]["winrate"]);
            newRow.appendChild(createCell(wins));
            let losses = platformCharacters[i]["matches"] - wins;
            newRow.appendChild(createCell(losses));
            tbody.appendChild(newRow);
        }
    }
    let container = document.querySelector("tbody.matchup_data");
    let nodata = document.querySelector("tr.nodata");
    nodata.style.display = "table-row";
    container.innerHTML = "";
    if (!(selectedCharacter in characterMap)) {
        return;
    }
    let selectedCharacterData = characterMap[selectedCharacter][selectedPlatform];
    if (selectedCharacterData) {
        nodata.style.display = "none";
        {
            let newRow = document.createElement("tr");
            newRow.appendChild(createCell("Overall"));
            newRow.appendChild(createCell(selectedCharacterData["totalMatches"]));
            newRow.appendChild(createCell(selectedCharacterData["overallWinrate"]));
            let wins = Math.round(selectedCharacterData["totalMatches"] * selectedCharacterData["overallWinrate"]);
            newRow.appendChild(createCell(wins));
            let losses = selectedCharacterData["totalMatches"] - wins;
            newRow.appendChild(createCell(losses));
            container.appendChild(newRow);
        }
        let matchups = selectedCharacterData["matchups"];
        matchups.sort((a, b) => {
            return b["matches"] - a["matches"];
        });
        for (let i = 0; i < matchups.length; i++) {
            let matchupDataRow = matchups[i];
            let newRow = document.createElement("tr");
            newRow.appendChild(createCell("vs " + matchupDataRow["vs"]));
            newRow.appendChild(createCell(matchupDataRow["matches"]));
            newRow.appendChild(createCell(matchupDataRow["winrate"]));
            let wins = Math.round(matchupDataRow["matches"] * matchupDataRow["winrate"]);
            newRow.appendChild(createCell(wins));
            let losses = matchupDataRow["matches"] - wins;
            newRow.appendChild(createCell(losses));
            container.appendChild(newRow);
        }
    }
}

renderData();

document.querySelector("#character").addEventListener("change", renderData);
document.querySelector("#platform").addEventListener("change", renderData);