{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "cca80000",
   "metadata": {},
   "outputs": [],
   "source": [
    "retirement_age = 65\n",
    "class Person:\n",
    "    def __init__(self, age, employed):\n",
    "        self.age = age\n",
    "        self.employed = employed\n",
    "\n",
    "    def update_age(self):\n",
    "        self.age += 1\n",
    "\n",
    "    def is_newborn(self):\n",
    "        return self.age == 0\n",
    "\n",
    "    def is_young(self):\n",
    "        return self.age < 15\n",
    "\n",
    "    def is_workforce(self):\n",
    "        return 14 < self.age < retirement_age\n",
    "\n",
    "    def is_senior(self):\n",
    "        return self.age >= retirement_age\n",
    "\n",
    "    def is_unemployed(self):\n",
    "        return not self.employed\n",
    "\n",
    "    def is_employed(self):\n",
    "        return self.employed"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
