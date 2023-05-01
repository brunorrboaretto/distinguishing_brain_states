import numpy as np 

StatsBlock= 3

perm_list = [21,22,23,24,25,26,27,28,
             29,30,31,32,33,34,35,36,
             37,38,0,1,2,3,4,5,
             6,39,42,40,7,8,9,10,
             11,12,13,41,43,44,14,15,
             16,17,18,19,20,45,46,47,
             48,49,50,51,52,53,54,55,
             56,57,58,59,60,61,62,63]



def perm_indices(ts, wl, lag):
	m = len(ts)-(wl-1)*lag
	indcs = np.zeros(m, dtype=int)
	for i in range(1, wl):
		st = ts[(i-1)*lag: m + ((i-1)*lag)]
		for j in range(i, wl):
			indcs += st > ts[j*lag: m+j*lag]
		indcs *= wl-i
	return indcs + 1

def complexity(P):
    ns = np.math.factorial(StatsBlock)  
    S = 0.0
    for i in range(ns):
        if P[i]!= 0.0:
            S-=(P[i]*np.log(P[i]))
    Pe = 1/ns
    Q0 = -2*(((ns+1)/ns)*np.log(ns+1)-2*np.log(2*ns)+np.log(ns))**(-1)
    S2 = 0.0
    for i in range(ns):
        S2-=(((P[i]+Pe)/2)*np.log((P[i]+Pe)/2))
    
    Q = Q0*(S2 - S/2 - np.log(ns)/2)
    return S/np.log(ns), Q*S/np.log(ns)

black_list = [97,109]
num_states = np.math.factorial(StatsBlock)

fp_out_1 = 'perm_spatial_S_raw_ec.npy'
fp_out_2 = 'perm_spatial_S_raw_eo.npy'

fp_out_3 = 'perm_spatial_S_alpha_ec.npy'
fp_out_4 = 'perm_spatial_S_alpha_eo.npy'

raw_ec = []

for i in range(1,110):
    print('perm raw EC',i)
    if i not in black_list:
        data = np.load('raw_data/data_ec_%.3d.npy' % i)
        data_aux = np.zeros((9600,64))
        for i in range(data.shape[1]):
            data_aux[:,i] = data[:,perm_list[i]]
        Size = data.shape[1]
        Aux = []
        for j in range(data.shape[0]):
            Serie = data_aux[j,:]                               
            Serie=(Serie-np.mean(Serie))/np.std(Serie)       
            a1 = perm_indices(Serie, StatsBlock, 1)
            hist = np.histogram(a1,num_states)
            P = 1.0*hist[0]/len(a1)
            H,C = complexity(P)
            Aux.append(H)
        raw_ec.append(Aux)

raw_eo = []

for i in range(1,110):
    print('perm raw EO',i)
    if i not in black_list:
        data = np.load('raw_data/data_eo_%.3d.npy' % i)
        data_aux = np.zeros((9600,64))
        for i in range(data.shape[1]):
            data_aux[:,i] = data[:,perm_list[i]]
        Size = data.shape[1]
        Aux = []
        for j in range(data.shape[0]):
            Serie = data_aux[j,:]                                  
            Serie=(Serie-np.mean(Serie))/np.std(Serie)       
            a1 = perm_indices(Serie, StatsBlock, 1)
            hist = np.histogram(a1,num_states)
            P = 1.0*hist[0]/len(a1)
            H,C = complexity(P)
            Aux.append(H)
        raw_eo.append(Aux)
           
alpha_ec = []

for i in range(1,110):
    print('perm alpha EC',i)
    if i not in black_list:
        data = np.load('filtered_data/alpha_data_ec_%.3d.npy' % i)
        data_aux = np.zeros((9600,64))
        for i in range(data.shape[1]):
            data_aux[:,i] = data[:,perm_list[i]]
        Size = data.shape[1]
        Aux = []
        for j in range(data.shape[0]):
            Serie = data_aux[j,:]                                  
            Serie=(Serie-np.mean(Serie))/np.std(Serie)       
            a1 = perm_indices(Serie, StatsBlock, 1)
            hist = np.histogram(a1,num_states)
            P = 1.0*hist[0]/len(a1)
            H,C = complexity(P)
            Aux.append(H)
        alpha_ec.append(Aux)

alpha_eo = []

for i in range(1,110):
    print('perm alpha EO',i)
    if i not in black_list:
        data = np.load('filtered_data/alpha_data_eo_%.3d.npy' % i)
        data_aux = np.zeros((9600,64))
        for i in range(data.shape[1]):
            data_aux[:,i] = data[:,perm_list[i]]
        Size = data.shape[1]
        Aux = []
        for j in range(data.shape[0]):
            Serie = data_aux[j,:]                                  
            Serie=(Serie-np.mean(Serie))/np.std(Serie)       
            a1 = perm_indices(Serie, StatsBlock, 1)
            hist = np.histogram(a1,num_states)
            P = 1.0*hist[0]/len(a1)
            H,C = complexity(P)
            Aux.append(H)
        alpha_eo.append(Aux)

raw_ec = np.array(raw_ec)
raw_eo = np.array(raw_eo)
alpha_ec = np.array(alpha_ec)
alpha_eo = np.array(alpha_eo)

print(raw_ec.shape)
print(raw_eo.shape)
print(alpha_ec.shape)
print(alpha_eo.shape)

np.save(fp_out_1,raw_ec)
np.save(fp_out_2,raw_eo)
np.save(fp_out_3,alpha_ec)
np.save(fp_out_4,alpha_eo)