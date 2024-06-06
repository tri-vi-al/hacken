from selenium import webdriver

# Pfad zum Chrome Webdriver anpassen
driver_path = '/Pfad/zum/chromedriver'
# Initialisierung des Chrome Webdrivers
driver = webdriver.Chrome('./chromedriver_win32')

# Webseite aufrufen
driver.get('https://www.new-vereinsfoerderung.de/projekte/661d89da7cdbeecc0e7e7b30')
s
# Wartezeit, um sicherzustellen, dass die Seite vollständig geladen ist
driver.implicitly_wait(10)

# Nachdem du die gewünschten Aktionen auf der Webseite durchgeführt hast, kannst du den WebDriver schließen
# driver.quit()
