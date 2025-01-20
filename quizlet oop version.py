from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QCheckBox
from PyQt6.QtCore import QTimer
from random import choice, shuffle

RIGHT = '✅'
WRONG = '❌'
correct_marker = '– xxx'
questions = {
    '1)According to the Taylor rule, what implies a level of output lower than the target?': ["the need to increase the interest rate.", "the need of fiscal policy.", "the need to decrease output.", "the need to cut the interest rate – xxx"],
    '2)What is a Credit Crunch?': ["economic activity declines.", "financial markets stop functioning affecting economic activity.", "interbank markets need to help the financial transactions.", "banks stop lending to firms. – xxx"],
    '3)The Distinction Between Real and Nominal Interest Rates is… ': ["Nominal interest rate makes allowance for inflation.", "Nominal interest rate makes no allowance for inflation. – xxx", "Real interest rate is higher than the nominal interest rate.", "Nominal interest rates are decided by the markets."],
    '4)What is the interbank market?': ["A liquidity exchange channel between businesses and banks.", "A channel of exchange of liquidity between banks.", "A channel of exchange of securities and liquidity between banks – xxx", "A channel of exchange of securities between different markets."],
    '5) ________ is a flow of earnings per unit of time.': ["Income – xxx", "Money", "Wealth", "Currency"],
    '6) Which of the following central banks is responsible of the monetary policy in Europe? ': ["FED.", "ECB. – xxx", "Bank of Italy.", "Bank of Spain."],
    '7)According to the Taylor rule, what implies a level of inflation higher than the target?': ["the need to increase the interest rate. – xxx", "the need of fiscal policy.", "the need to decrease output.", "the need to cut the interest rate."],
    '8)The spread between the interest rates on bonds with default risk and default-free bonds is called the': ["risk premium. – xxx", "junk margin.", "bond margin.", "default premium."],
    '9)A financial crisis occurs when…': ["there is a particularly large disruption to information flows in financial markets. – xxx", "there are fiscal imbalances.", "there is a free-rider problem.", "there is full information."],
    '10)A serious consequence of a financial crisis is:':['A contraction in economic activity. – xxx', 'An increase in asset prices.', 'Financial engineering.', 'Financial globalization.'],
    '11)A major disruption in financial markets characterized by sharp declines in asset prices and firm failures is called a': ["a contraction in economic activity. – xxx", "an increase in asset prices.", "financial engineering.", "financial globalization."],
    '12)In developed economies Monetary Policy could work better if:': ["Financial markets are developed.", "The unemployment is low.", "The banking sector sets competitive interest rates. – xxx", "If banks lend less to firms."],
    '13)Consider the real and the nominal interest rate of a security (i.e. the three month treasury bill)in a given period of time': ["they show the same trend. – xxx", "they move quite differently.", "They are not affected by inflation.", "They are both affected by inflation."],
    '14)Financial markets promote economic efficiency by': ["channeling funds from investors to savers.", "creating inflation.", "channeling funds from savers to investors. – xxx", "reducing investment."],
    '15)Well-functioning financial markets promote': ["inflation.", "deflation.", "unemployment.", "growth. – xxx"],
    '16)Well-functioning financial markets promote': ["inflation", "financial integration", "unemployment", "development – xxx"],
    '17)The price paid for the rental of borrowed funds (usually expressed as a percentage of the rental of $100 per year) is commonly referred to as the': ["inflation rate.", "exchange rate.", "interest rate. – xxx", "aggregate price level."],
    '18)Every financial market has the following characteristic': ["It determines the level of interest rates.", "It allows common stock to be traded.", "It allows loans to be made.", "It channels funds from lenders-savers to borrowers-spenders. – xxx"],
    '19)The government agency that oversees the banking system and is responsible for the conduct of monetary policy in the United States is': ["the Federal Reserve System. – xxx", "the United States Treasury.", "the U.S. Gold Commission.", "the House of Representatives."],
    '20)Everything else held constant, aggregate demand increases when': ["taxes are cut. – xxx", "government spending is reduced.", "animal spirits decrease.", "the money supply is reduced."],
    '21)If you invest in the bank for 2 consecutive years $ 100 at the 3% risk-free rate, what do you get when you withdraw it all?': ["98.0296", "103.03", "101", "106.09 – xxx"],
    '22)What is the present value of $200.00 that you will receive in two years if the interest rate is 5%?': ["$190.475", "$200", "$191.406", "$181.406 – xxx"],
    '23)When does the ECB increase policy interest rates?': ["When the output declines.", "When the financial markets are imperfect", "When inflation increases – xxx", "When banks stop lending to firms"],
    '24)What was the monetary response of the FED to the Covid19 emergency?': ["The FED kept the monetary policy unchanged", "The FED has expanded its balance sheet to intervene – xxx", "The FED has restricted its balance sheet to save money", "The FED stopped lending in the interbank market"],
    '25) Monetary policy in Europe is not concerned with ESG?':['Yes',f'No {correct_marker}', 'maybe', 'probably not'],
    '26)Why regulation of financial intermediaries is needed?': ["To protect banks", "To avoid insider trading", "To increase the information available to investors and to ensure financial stability – xxx", "To allow diversification"],
    '27)Which of the following variables is not included in the Taylor Rule?':[f'The unemployment gap {correct_marker}', f'The inflation rate', f'The output gap', f'The inflation target'],
    '28)Which of this is not a monetary policy in the strict sense and according to formal definitions.':["Newly issued government bonds",'Withdrawal of government bonds from the market', 'Loans to banks at policy rates by the Central Bank.', f'Commercial bank transactions {correct_marker}'],
    '29)Normally, the long-term interest rate of a security': ['it is lower than the short-term rate','it is equal to the risk-free rate','it decreases as the security risk increases',f'it is higher than the short-term rate{correct_marker}'],
    '30)Monetary Policy in Europe is actually coordinated with fiscal policy at Central Level?': ['YES','Sometimes' ,f'NO {correct_marker}' ,'only regarding exports'],
    '31)Monetary Policy in Europe is concerned only with inflation':['YES','Sometimes' ,f'NO {correct_marker}' ,'only regarding exports'],
    '32)What is a G-SIFI?':[f'Indicates the banks of "systemic interest" at the global financial level. {correct_marker}', 'Means local “systemic” banks.', 'They have fewer requirements for regulatory capital.', 'They are more prone to failure'],
    '33)What is an interbank market freeze?':['ECB stops lending', 'Financial markets stop functioning', 'Interbank markets help the financial transactions.', f'The interbank channel stops lending to troubled banks {correct_marker}'],
    '34)Financial Crises in Emerging Economies, unlike crises in developed countries':['They recover faster', 'They have high unemployment rate', 'theya re often accompanied by economic crises', f'they are often accompanied by exchange rate crises {correct_marker}'],
    '35)What is the actual monetary response of the FED to the inflation emergency':['The FED kept the monetary policy unchanged.', f'The FED has increased its policy rates {correct_marker}', 'Policy rates have been cut by the FED.', 'The FED stopped lending in the interbank market'],
    '36)The classical theory of neutrality of money implies..':[f'monetary policies have no real effect in the short run and also no real effect in the long run {correct_marker}', 'monetary policies do not have real effects in the long run but they can havethem in the short run.', 'monetary policies have real effects both in the long run and in the short run', 'mmonetary policies do not affect prices'],
    '37)WHat is money?':['the total collection of pieces of property that serve to store value','a collection of banknotes and coins','total wealth',f'anything that is generally accepted as payment for goods or services or in the repayment of debts {correct_marker}'],
    '38)What is an assumption of the quantity theory of money?':["The velocity of circulation of money is changing in the short run","Output is affected by the money supply",f'Changes in money supply affect only the price level {correct_marker}','Movement in prices are random'],
    '39)What is financial innovation?':['financial services',f'the development of new financial products and services {correct_marker}','interdependence between financial instruments','financial integration'],
    '40)Which of these functions do modern central banks not support':['Financial stability','Economic growth','Pandemic recovery',f'Political stability {correct_marker}'],
    '41)Monetary Policies in Europe could work better if':[f'it is coordinated with fiscal policy {correct_marker}','The governments communicated better','Choco was King','There was more political syability'],
    '42)What was the first official ECB mandate?':['Financial stability','Economic growth',f'inflation maintenance around 2% {correct_marker}','To decerease unemploymeny'],
    '43)Why regulation of financial intermediaries is needed?':['to protect banks','to avoid insider trading',f'to increase the information available to investors and to ensure financial stabilitry {correct_marker}','to allow diversification']

}
first_q = choice(list(questions.keys()))
app = QApplication([])

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Quizlet')
        self.setGeometry(100, 100, 500, 500)
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.label = QLabel(f"{first_q}", parent=self)
        self.label_font = self.label.font()
        self.label_font.setPointSize(20)
        self.label.setFont(self.label_font)
        self.checkbox_1 = QCheckBox(f"{questions[first_q][0].replace(correct_marker, '')}", parent=self)
        self.checkbox_2 = QCheckBox(f"{questions[first_q][1].replace(correct_marker, '')}", parent=self)
        self.checkbox_3 = QCheckBox(f"{questions[first_q][2].replace(correct_marker, '')}", parent=self)
        self.checkbox_4 = QCheckBox(f"{questions[first_q][3].replace(correct_marker, '')}", parent=self)
        self.checkbox_list = [self.checkbox_1, self.checkbox_2, self.checkbox_3, self.checkbox_4]
        self.button = QPushButton('Next')
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.checkbox_1)
        self.layout.addWidget(self.checkbox_2)
        self.layout.addWidget(self.checkbox_3)
        self.layout.addWidget(self.checkbox_4)
        self.layout.addWidget(self.button)
        self.reformat_answers()
        self.show()

    def reformat_answers(self):
        for checkbox in self.checkbox_list:
            cb_font = checkbox.font()
            cb_font.setPointSize(15)
            checkbox.setFont(self.label_font)

    def change_question(self):
        current_q = self.label.text()
        questions.pop(current_q)
        new_q = choice(list(questions.keys()))
        self.label.setText(new_q)
        new_q_set = questions[new_q]
        shuffle(new_q_set)
        a_pos = 0
        for checkbox in self.checkbox_list:
            if checkbox.isChecked(): checkbox.setChecked(False)
            checkbox.setText(new_q_set[a_pos].replace(correct_marker, ''))
            a_pos += 1

    def button_clicked(self):
        # checks if correct
        wrong_answer = False
        checked = False
        for checkbox in self.checkbox_list:
            if checkbox.isChecked():
                checked = True
                if checkbox.text() not in questions[self.label.text()]:
                    curr_text = checkbox.text()
                    checkbox.setText(f'{curr_text} {RIGHT}')
                    print(f"Correct!")
                    break
                else:
                    curr_text = checkbox.text()
                    checkbox.setText(f'{curr_text} {WRONG}')
                    wrong_answer = True
                    print(
                        f"Wrong! {[answer for answer in questions[self.label.text()] if answer.endswith(correct_marker)][0].replace(correct_marker, '')}")
                    break
        if not checked: print("No answer:(")
        if wrong_answer:
            pass
        QTimer.singleShot(1000, self.change_question)


window = Window()
window.button.clicked.connect(window.button_clicked)
app.exec()