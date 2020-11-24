#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Sanitation Explorer: Sustainable design of non-sewered sanitation technologies
Copyright (C) 2020, Sanitation Explorer Development Group

This module is developed by:
    Yalin Li <zoe.yalin.li@gmail.com>

This module is under the UIUC open-source license. Please refer to 
https://github.com/QSD-for-WaSH/sanitation/blob/master/LICENSE.txt
for license details.

Ref:
    [1] Trimmer et al., Navigating Multidimensional Social–Ecological System
        Trade-Offs across Sanitation Alternatives in an Urban Informal Settlement.
        Environ. Sci. Technol. 2020, 54 (19), 12641–12653.
        https://doi.org/10.1021/acs.est.0c03296.

'''

# %%

import numpy as np

__all__ = ('Decay',)


# %%

#!!! This can be potentially made into a Process
class Decay:
    '''For non-steady state degradation.'''

    def __init__(self):
        self._COD_max_removal = None
        self._decay_k_COD = None
        self._MCF_decay = None
        self._max_CH4_emission = None
        self._N_max_removal = None
        self._decay_k_N = None
        self._N2O_EF_decay = None

    @staticmethod
    def allocate_N_removal(tot_red, NH3):
        '''
        Allocate the total amount of N removal to NH3 and non-NH3 Components.
        NH3 will be firstly removed before non-NH3.

        Parameters
        ----------
        tot_red : [float]
            Total amount of N to be removed.
        NH3 : [float]
            Current NH3 content.

        Returns
        -------
        [float]
            Amount of NH3 to be removed.
        [float]
            Amount of non-NH3 to be removed.

        '''
        if not NH3 > 0:
            return 0, tot_red
        elif NH3 > tot_red:
            return tot_red, 0
        else:
            return NH3, tot_red-NH3  
      
    @staticmethod
    def first_order_decay(k, t, max_removal, t0=0, tot=1):
        '''
        Calculate first-order degradation loss based on ref [1].
        
        .. math::
            C_0 = tot * max_removal
            C_avg = C_0/(k*t) * (e^{-k*t_0}-e^{-k*t_f})
            loss = C_0 - C_avg

        Parameters
        ----------
        k : [float]
            Degradation rate constant.
        t0 : [float]
            Degradation time prior to current process.
        t : [float]
            Degradation time in current process.
        max_removal : [float]
            Maximum removal ratio.
        tot : [float], optional
            Total degradable amount.
            If set to 1 (default), the return is the relative ratio (i.e., loss/tot).

        Returns
        -------
        loss : [float]
            Amount lost due to degradation.

        '''

        C0 = tot * max_removal
        Cavg = C0/(k*t) * (np.exp(-k*t0)-np.exp(-k*(t0+t)))
        loss = C0 - Cavg
        return loss


    @property
    def COD_max_removal(self):
        '''[float] Maximum fraction of COD removed during storage given sufficient time.'''
        return self._COD_max_removal
    @COD_max_removal.setter
    def COD_max_removal(self, i):
        self._COD_max_removal = float(i)

    @property
    def decay_k_COD(self):
        '''[float] Rate constant for COD decay.'''
        return self._decay_k_COD
    @decay_k_COD.setter
    def decay_k_COD(self, i):
        self._decay_k_COD = float(i)

    @property
    def MCF_decay(self):
        '''[float] Methane correction factor for COD decay.'''
        return self._MCF_decay
    @MCF_decay.setter
    def MCF_decay(self, i):
        self._MCF_decay = float(i)

    @property
    def max_CH4_emission(self):
        '''[float] Maximum methane emssion as a fraction of degraded COD, [g CH4/g COD].'''
        return self._max_CH4_emission
    @max_CH4_emission.setter
    def max_CH4_emission(self, i):
        self._max_CH4_emission = float(i)

    @property
    def N_max_removal(self):
        '''[float] Maximum fraction of N removed through denitrification during storage given sufficient time.'''
        return self._N_max_removal
    @N_max_removal.setter
    def N_max_removal(self, i):
        self._N_max_removal = float(i)

    @property
    def decay_k_N(self):
        '''[float] Rate constant for N decay.'''
        return self._decay_k_N
    @decay_k_N.setter
    def decay_k_N(self, i):
        self._decay_k_N = float(i)

    @property
    def N2O_EF_decay(self):
        '''[float] Fraction of N emitted as N2O during decay.'''
        return self._N2O_EF_decay
    @N2O_EF_decay.setter
    def N2O_EF_decay(self, i):
        self._N2O_EF_decay = float(i)







