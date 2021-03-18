{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "check-permutation.py",
      "provenance": [],
      "authorship_tag": "ABX9TyNuoDCjFsRzjcohwkc8wHHW",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/mikaeelkhalid/coding-practice/blob/main/check_permutation_py.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "xJkMbzn6ellm"
      },
      "source": [
        "**Check Permutation: Given two strings, write a method to decide if one is a permutation of the other.**\n"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "j_CK1AG_eoxB",
        "outputId": "a5e24d46-db1a-440d-fded-893e5a7c9706"
      },
      "source": [
        "def check_permutation_by_sort(s1, s2):\n",
        "  if len(s1) != len(s2):\n",
        "    return False\n",
        "\n",
        "  s1, s2 = sorted(s1), sorted(s2)\n",
        "\n",
        "  for i in range(len(s1)): # O(n)\n",
        "    if s1[i] != s2[i]:\n",
        "      return False\n",
        "  return True\n",
        "\n",
        " \n",
        "check_permutation_by_sort(\"abcd\", \"bacd\")"
      ],
      "execution_count": 3,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "True"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 3
        }
      ]
    }
  ]
}