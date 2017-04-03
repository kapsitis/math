/**
 * Created by kalvis on 17.2.4.
 */

var tag = document.createElement('script');

tag.src = "https://www.youtube.com/iframe_api";
var firstScriptTag = document.getElementsByTagName('script')[0];
firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);

var player;
function onYouTubeIframeAPIReady() {
    player = new YT.Player('player', {
        height: '390',
        width: '640',
        //        videoId: 'tWx-UGFeuSA',
        videoId: myVideoId,
        events: {
            'onReady': onPlayerReady,
            'onStateChange': onPlayerStateChange
        }
    });
}

function onPlayerReady(event) {
    //        event.target.playVideo();
}

var done = false;
function onPlayerStateChange(event) {
    //        if (event.data == YT.PlayerState.PLAYING && !done) {
    //          setTimeout(stopVideo, 6000);
    //          done = true;
    //        }
}
function stopVideo() {
    player.stopVideo();
}

function jumpIntoVideo(sss) {
    player.seekTo(sss, true);
    return false;
}

var myProblems = [{
    "title": "Ao2011.5.1",
    "videoId": "tWx-UGFeuSA",
    "problemText": ["Reizināšanas piemērā ciparus aizstāja ar burtiem un ieguva izteiksmi", "$$AB \\cdot CD = EEE.$$", "Atjauno sākotnējo reizināšanas piemēru, ja zināms, ka vienādi burti", "apzīmē vienādus ciparus, bet dažādi burti – dažādus ciparus,", "pie tam ne $A$, ne $C$ nav $0$. Atrodi visus iespējamos atrisinājumus!"],
    "annotationSets": [{
        "subtitle": "Uzdevuma saprašana",
        "bookmarks": [{ "mmss": "00:05", "text": "Piemērā abi reizinātāji ir īsti divciparu skaitļi." }, { "mmss": "00:45", "text": "Kādēļ pilnā pārlase neder." }, { "mmss": "01:18", "text": "Izmantojam vienādības labo pusi, lai samazinātu meklējumu telpu." }]
    }, {
        "subtitle": "Risināšanas plāns",
        "bookmarks": [{ "mmss": "02:00", "text": "Skaitļa $111$ izteikšana ar reizinājumu. Metode: Dalīšana pirmreizinātājos." }, { "mmss": "02:55", "text": "Izsakām visus $EEE$ skaitļus kā reizinājumus. Metode: Gadījumu pārlase." }, { "mmss": "03:40", "text": "Kādēļ kreisajā pusē jābūt $37$ vai $74$? Metode: Dalāmība veselu skaitļu vienādojumā." }, { "mmss": "05:43", "text": "Nederīgo reizinājumu atmešana. Metode: Izslēgšanas metode." }]
    }, {
        "subtitle": "Atskats",
        "bookmarks": [{ "mmss": "07:08", "text": "Atbildes formulējums; reizinātāju mainīšana vietām atbilžu skaitu formāli palielina." }]
    }]
}];

/*
https://facebook.github.io/react/docs/handling-events.html
http://stackoverflow.com/questions/27707911/add-event-handler-to-react-dom-element-dynamically
*/

function initVideo() {

    var ProblemStuff = React.createClass({

        actionLink: function (i, j, sss) {
            return React.createElement("a", {
                "href": "#",
                onClick: function (e) {
                    e.preventDefault();
                    player.seekTo(sss, true);
                }.bind(this)
            }, myProblems[0]["annotationSets"][i]["bookmarks"][j]["text"]);
        },

        renderItems: function () {
            var result = [];
            for (var i = 0; i < myProblems[0]["annotationSets"].length; i++) {
                result.push(React.createElement("div", { className: "line" }, React.createElement("b", {}, myProblems[0]["annotationSets"][i]["subtitle"])));
                for (var j = 0; j < myProblems[0]["annotationSets"][i]["bookmarks"].length; j++) {
                    var mmss = myProblems[0]["annotationSets"][i]["bookmarks"][j]["mmss"].split(":");
                    var sss = parseInt(mmss[0], 10) * 60 + parseInt(mmss[1], 10);
                    result.push(React.createElement("div", { className: "indentedLine" }, React.createElement("span", {}, myProblems[0]["annotationSets"][i]["bookmarks"][j]["mmss"] + "\u00A0"), this.actionLink(i, j, sss)));
                }
            }
            return result;
        },

        render: function () {
            return React.createElement("div", { className: "ee" }, React.createElement("div", { className: "problem", "id": "MathExample" }, myProblems[0]["problemText"].join(" ")), React.createElement.apply(this, ["div", { className: "timeLinks" }].concat(this.renderItems())), React.createElement("p", { "style": { "marginTop": "5px" } }, React.createElement("b", {}, "Norādes: "), React.createElement("a", {
                "href": "http://nms.lu.lv/uzdevumu-arhivs/latvijas-olimpiades/"
            }, "Latvijas olimpiāžu uzdevumu arhīvs")));
        }
    });

    React.render(React.createElement(ProblemStuff), document.getElementById("problemStuff"));

    MathJax.Hub.Queue(["Typeset", MathJax.Hub]);
}
//# sourceMappingURL=video-init.js.map
