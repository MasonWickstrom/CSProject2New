from PyQt6.QtWidgets import *
from Proj2gui import *
import csv


class Logic(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.balance = 0
        self.deposit_count = 0

        self.submitButton.clicked.connect(lambda: self.submit())
        self.logOutButton.clicked.connect(lambda: self.logOut())
        self.submitButton2.clicked.connect(lambda: self.submit2())

    def submit(self):
        name = self.typeName.text()
        password = self.typePassword.text()
        passwordCheck = self.typePasswordCheck.text()
        if name == '':
            self.accountPageGuide.setText('Please enter a name for the account.')
        elif password == '':
            self.accountPageGuide.setText('Please enter a password.')
        elif passwordCheck != password:
            self.wrongPasswordLabel.setVisible(True)
        else:
            self.submitButton.setVisible(False)
            self.accountLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
            self.accountLabel.setGeometry(QtCore.QRect(0, 35, 300, 10))
            self.accountLabel.setText(f'Account Name: {name}')
            self.accountPageGuide.setText('Choose an option below.')
            self.passwordLabel.setVisible(False)
            self.typePassword.setVisible(False)
            self.typeName.setVisible(False)
            self.savingsCheckBox.setVisible(False)
            self.checkPasswordLabel.setVisible(False)
            self.typePasswordCheck.setVisible(False)
            self.wrongPasswordLabel.setVisible(False)
            self.depositButton.setVisible(True)
            self.withdrawalButton.setVisible(True)
            self.amountLabel.setVisible(True)
            self.amountInput.setVisible(True)
            self.balanceLabel.setText(f'Account balance = ${self.balance:.2f}')
            self.submitButton2.setVisible(True)
            self.logOutButton.setVisible(True)

    def logOut(self):
        self.submitButton.setVisible(True)
        self.accountLabel.setGeometry(QtCore.QRect(10, 35, 80, 10))
        self.accountLabel.setText('Account Name:')
        self.accountPageGuide.setText('Create an account.')
        self.passwordLabel.setVisible(True)
        self.typePassword.setVisible(True)
        self.typeName.setVisible(True)
        self.savingsCheckBox.setVisible(True)
        self.checkPasswordLabel.setVisible(True)
        self.typePasswordCheck.setVisible(True)
        self.wrongPasswordLabel.setVisible(False)
        self.depositButton.setChecked(False)
        self.depositButton.setVisible(False)
        self.withdrawalButton.setChecked(False)
        self.withdrawalButton.setVisible(False)
        self.amountLabel.setVisible(False)
        self.amountInput.setVisible(False)
        self.submitButton2.setVisible(False)
        self.logOutButton.setVisible(False)
        self.typeName.setText('')
        self.typePassword.setText('')
        self.typePasswordCheck.setText('')
        self.savingsCheckBox.setChecked(False)
        self.balanceLabel.setText('')
        self.amountInput.setText('')
        self.balance = 0

    def submit2(self):
        if self.savingsCheckBox.isChecked():
            try:
                amount = float(self.amountInput.text())
                if self.depositButton.isChecked():
                    if self.deposit_save(amount) is False:
                        self.accountPageGuide.setText('Please determine an amount.')
                    else:
                        balance = self.balance
                        self.balanceLabel.setText(f'Account balance = ${balance:.2f}')
                elif self.withdrawalButton.isChecked():
                    if self.withdraw_save(amount) is False:
                        self.accountPageGuide.setText('Please determine an amount.')
                    else:
                        balance = self.balance
                        self.balanceLabel.setText(f'Account balance: ${balance:.2f}')
                else:
                    self.accountPageGuide.setText('Please deposit or withdraw.')
            except ValueError:
                self.accountPageGuide.setText('Please determine an amount.')
        else:
            try:
                amount = float(self.amountInput.text())
                if self.depositButton.isChecked():
                    if self.deposit(amount) is False:
                        self.accountPageGuide.setText('Please determine an amount.')
                    else:
                        balance = self.balance
                        self.balanceLabel.setText(f'Account balance = {balance:.2f}')
                elif self.withdrawalButton.isChecked():
                    if self.withdraw(amount) is False:
                        self.accountPageGuide.setText('Please determine an amount.')
                    else:
                        balance = self.balance
                        self.balanceLabel.setText(f'Account balance: {balance:.2f}')
                else:
                    self.accountPageGuide.setText('Please deposit or withdraw.')
            except ValueError:
                self.accountPageGuide.setText('Please determine an amount.')

    def deposit(self, amount):
        if amount <= 0:
            return False
        else:
            self.balance += amount
            return True

    def withdraw(self, amount):
        if amount <= 0 or amount >= self.balance:
            return False
        else:
            self.balance -= amount
            return True

    def apply_interest(self):
        self.deposit(self.balance * 0.02)

    def deposit_save(self, amount):
        if amount <= 0:
            return False
        else:
            self.deposit(amount)
            self.deposit_count += 1
            if self.deposit_count == 5:
                self.deposit_count -= 5
                self.apply_interest()
            return True

    def withdraw_save(self, amount):
        if self.balance - amount >= 100:
            self.withdraw(amount)
            return True
        else:
            return False
