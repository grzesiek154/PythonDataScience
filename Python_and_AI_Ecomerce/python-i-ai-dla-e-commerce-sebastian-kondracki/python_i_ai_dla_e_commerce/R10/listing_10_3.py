from bs4 import BeautifulSoup

html = """
      <!DOCTYPE>
      <html>
        <head><title>Selectors</title></head>
          <body>
            <div class="header"><p>Witaj! Sebastian</p></div>
            <div class="message nice"><span class="red">Milutki</span>użytkownik</div>
            <div id="email">sebastian@zazepa.pl</div>
            <div>Wstęp</div><p>Paragraf 1.</p><p>Paragraf 2.</p>
            <a href="koszyk.php" title="Dodaj do koszyka">Dodaj do koszyka></a>
            <img src="1.png" alt="Piękny obrazek" width="100"/>
            <a href="strona-glowna.php">HOME></a>
            <strong>
              Linia 1
              Linia 2
            </strong>
            </body>
        </html> 
"""

def show_test_summary(name, elements):
    tags = ", ".join([item.name for item in elements])
    print('{}: liczba znaczników {}, znaczniki {}'.format(name, len(elements), tags))

page = BeautifulSoup(html, "html.parser")
show_test_summary("TEST SELEKTORA *", page.select("*"))
show_test_summary("TEST SELEKTORA #identyfikator",
page.select("#email"))
show_test_summary("TEST SELEKTORA .klasa", page.select(".header"))
show_test_summary("TEST SELEKTORA .klasa1.klasa2",
page.select(".nice.message"))
show_test_summary("TEST SELEKTORA znacznik", page.select("p"))
show_test_summary("TEST SELEKTORA znacznik.klasa",
page.select("span.red"))
show_test_summary("TEST SELEKTORA znacznik1,znacznik2",
page.select("span,p"))
show_test_summary("TEST SELEKTORA znacznik1+znacznik2",
page.select("div+p"))
show_test_summary("TEST SELEKTORA znacznik1>znacznik2",
page.select("div>p"))
show_test_summary("TEST SELEKTORA znacznik1~znacznik2",
page.select("div~p"))
show_test_summary("TEST SELEKTORA [atrybut]", page.select("[title]"))
show_test_summary("TEST SELEKTORA [atrybut=wartość]",
page.select('[width="100"]'))
show_test_summary("TEST SELEKTORA [atrybut~=wartość]",
page.select('[title~="Dodaj"]'))
show_test_summary("TEST SELEKTORA [atrybut|=wartość]",
page.select('[href|="strona"]'))
show_test_summary("TEST SELEKTORA [atrybut*=wartość]",
page.select('[alt*="braz"]'))
show_test_summary("TEST SELEKTORA [atrybut$=wartość]",
page.select('[href$="php"]'))
show_test_summary("TEST SELEKTORA [atrybut^=wartość]",
page.select('[href^="koszyk"]'))
show_test_summary("TEST SELEKTORA znacznik:first-child",
page.select("div:first-child"))
show_test_summary("TEST SELEKTORA :not(selektor)",
page.select(":not(span.red)"))