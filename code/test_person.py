{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b2dcac48",
   "metadata": {},
   "outputs": [],
   "source": [
    "# use unittest\n",
    "import unittest\n",
    "from person import Person  # Import the Person class from person.py\n",
    "\n",
    "class TestPerson(unittest.TestCase):\n",
    "    def test_is_newborn(self):\n",
    "        newborn = Person(age=0, employed=False)\n",
    "        self.assertTrue(newborn.is_newborn())\n",
    "        self.assertFalse(newborn.is_young())\n",
    "        self.assertFalse(newborn.is_workforce())\n",
    "        self.assertFalse(newborn.is_senior())\n",
    "        self.assertTrue(newborn.is_unemployed())\n",
    "        self.assertFalse(newborn.is_employed())\n",
    "\n",
    "    def test_is_young(self):\n",
    "        young = Person(age=10, employed=False)\n",
    "        self.assertFalse(young.is_newborn())\n",
    "        self.assertTrue(young.is_young())\n",
    "        self.assertFalse(young.is_workforce())\n",
    "        self.assertFalse(young.is_senior())\n",
    "        self.assertTrue(young.is_unemployed())\n",
    "        self.assertFalse(young.is_employed())\n",
    "\n",
    "    def test_is_workforce(self):\n",
    "        workforce = Person(age=25, employed=False)\n",
    "        self.assertFalse(workforce.is_newborn())\n",
    "        self.assertFalse(workforce.is_young())\n",
    "        self.assertTrue(workforce.is_workforce())\n",
    "        self.assertFalse(workforce.is_senior())\n",
    "        self.assertTrue(workforce.is_unemployed())\n",
    "        self.assertFalse(workforce.is_employed())\n",
    "\n",
    "    def test_is_senior(self):\n",
    "        senior = Person(age=70, employed=False)\n",
    "        self.assertFalse(senior.is_newborn())\n",
    "        self.assertFalse(senior.is_young())\n",
    "        self.assertFalse(senior.is_workforce())\n",
    "        self.assertTrue(senior.is_senior())\n",
    "        self.assertTrue(senior.is_unemployed())\n",
    "        self.assertFalse(senior.is_employed())\n",
    "\n",
    "    def test_is_unemployed(self):\n",
    "        unemployed = Person(age=30, employed=False)\n",
    "        self.assertFalse(unemployed.is_unemployed())\n",
    "        employed = Person(age=40, employed=True)\n",
    "        self.assertFalse(employed.is_unemployed())\n",
    "\n",
    "    def test_is_employed(self):\n",
    "        employed = Person(age=50, employed=True)\n",
    "        self.assertTrue(employed.is_employed())\n",
    "        unemployed = Person(age=60, employed=False)\n",
    "        self.assertFalse(unemployed.is_employed())\n",
    "\n",
    "if __name__ == '__main__':\n",
    "    unittest.main()"
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
