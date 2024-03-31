from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import pyautogui
import pyautogui
import subprocess
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

keyword_to_url = {
    "openai": "https://openai.com",
    "google": "https://google.com",
    "github": "https://github.com",
    # Fügen Sie weitere Keywords und URLs hier hinzu
}



class ActionShowWindows(Action):
    def name(self) -> Text:
        return "action_show_windows"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # Windows-Tastenkombination, um alle Fenster anzuzeigen
        pyautogui.hotkey('win', 'd')
        dispatcher.utter_message(text="Alle Fenster werden angezeigt.")

        return []

class ActionMaximizeWindow(Action):
    def name(self) -> Text:
        return "action_maximize_window"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # Simuliert Alt + Leertaste gefolgt von 'x' um das Fenster zu maximieren
        pyautogui.hotkey('alt', 'space')
        pyautogui.press('x')
        dispatcher.utter_message(text="Aktuelles Fenster wird maximiert.")

        return []

class ActionCloseWindow(Action):
    def name(self) -> Text:
        return "action_close_window"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # Simuliert Alt + F4, um das aktuelle Fenster zu schließen
        pyautogui.hotkey('alt', 'f4')
        dispatcher.utter_message(text="Aktuelles Fenster wird geschlossen.")

        return []

class ActionSwitchToDesktop(Action):
    def name(self) -> Text:
        return "action_switch_to_desktop"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # Windows-Tastenkombination, um zum Desktop zu wechseln
        pyautogui.hotkey('win', 'd')
        dispatcher.utter_message(text="Wechsel zum Desktop.")

        return []

import webbrowser

def open_url_by_keyword(keyword):
    url = keyword_to_url.get(keyword)
    if url:
        webbrowser.open(url)
        return f"Öffne {url}"
    else:
        return "Keyword nicht gefunden. Bitte überprüfen Sie Ihre Eingabe."


class ActionOpenBrowser(Action):
    def name(self) -> Text:
        return "action_open_browser"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # Beispiel: Öffnen von Google Chrome. Passen Sie den Pfad an Ihre Installation an
        subprocess.Popen("C:/Program Files/Google/Chrome/Application/chrome.exe")
        dispatcher.utter_message(text="Browser wird geöffnet.")

        return []

class ActionOpenExplorer(Action):
    def name(self) -> Text:
        return "action_open_explorer"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        subprocess.Popen("explorer")
        dispatcher.utter_message(text="Explorer wird geöffnet.")

        return []

class ActionOpenCalculator(Action):
    def name(self) -> Text:
        return "action_open_calculator"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        subprocess.Popen("calc")
        dispatcher.utter_message(text="Taschenrechner wird geöffnet.")

        return []

class ActionOpenApplication(Action):
    def name(self) -> Text:
        return "action_open_application"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # Sie müssen den spezifischen Anwendungsnamen oder -pfad basierend auf der Benutzeranfrage extrahieren
        app_name = tracker.get_slot('application_name')
        if app_name:
            # Versuch, die Anwendung zu öffnen (Beispielhaft)
            try:
                subprocess.Popen(app_name)
                dispatcher.utter_message(text=f"{app_name} wird geöffnet.")
            except Exception as e:
                dispatcher.utter_message(text=f"Fehler beim Öffnen von {app_name}: {e}")
        else:
            dispatcher.utter_message(text="Anwendungsname nicht angegeben.")

        return []

class ActionCloseApplication(Action):
    def name(self) -> Text:
        return "action_close_application"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # Das Schließen einer Anwendung erfordert spezifischere Logik, die nicht direkt mit subprocess oder pyautogui umgesetzt werden kann.
        # Dies könnte mit systemnahen Befehlen wie `taskkill` unter Windows oder ähnlichen in anderen Betriebssystemen umgesetzt werden.
        app_name = tracker.get_slot('application_name')
        if app_name:
            try:
                # Beispiel für Windows
                subprocess.run(["taskkill", "/im", app_name + ".exe", "/f"], check=True)
                dispatcher.utter_message(text=f"{app_name} wird geschlossen.")
            except Exception as e:
                dispatcher.utter_message(text=f"Fehler beim Schließen von {app_name}: {e}")
        else:
            dispatcher.utter_message(text="Anwendungsname nicht angegeben.")

        return []
