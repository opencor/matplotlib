from __future__ import absolute_import, division, print_function

import six
import matplotlib.pyplot as plt


def test_stem_remove():
    ax = plt.gca()
    st = ax.stem([1, 2], [1, 2])
    st.remove()


def test_errorbar_remove():

    # Regression test for a bug that caused remove to fail when using
    # fmt='none'

    ax = plt.gca()

    eb = ax.errorbar([1], [1])
    eb.remove()

    eb = ax.errorbar([1], [1], xerr=1)
    eb.remove()

    eb = ax.errorbar([1], [1], yerr=2)
    eb.remove()

    eb = ax.errorbar([1], [1], xerr=[2], yerr=2)
    eb.remove()

    eb = ax.errorbar([1], [1], fmt='none')
    eb.remove()
