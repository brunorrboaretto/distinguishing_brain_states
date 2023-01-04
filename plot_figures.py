import matplotlib.pyplot as plt
import numpy as np
import sys

#plt.rcParams['text.usetex'] = True
#plt.rc('text.latex', preamble=r'\usepackage{siunitx}')
#plt.rc('font',**{'family':'serif','serif':['courier']})

sz1 = 30
sz2 = 25

X = np.linspace(0,60,9600)

fig = plt.figure()
print('Generating figure 1')

gs = fig.add_gridspec(2,3)
ax_0 = fig.add_subplot(gs[0,:-1])
ax_1 = fig.add_subplot(gs[0,-1])

ax_2 = fig.add_subplot(gs[1,:-1])
ax_3 = fig.add_subplot(gs[1,-1])

data_raw_ec = np.load('spatial_S_raw_ec.npy')
data_raw_eo = np.load('spatial_S_raw_eo.npy')
data_alpha_ec = np.load('spatial_S_alpha_ec.npy')
data_alpha_eo = np.load('spatial_S_alpha_eo.npy')

mean_1 = []
mean_2 = []

for i in range(len(X)):
    mean_1.append(np.mean(data_raw_ec[:,i]))
    mean_2.append(np.mean(data_raw_eo[:,i]))

mean_1 = np.array(mean_1)
mean_2 = np.array(mean_2)

ax_0.plot(X,mean_1,color='C0',alpha=0.85,label='EC')#,color='k',capsize=3)
ax_0.plot(X,mean_2,color='C1',alpha=0.85,label='EO')#,color='r',capsize=3)
ax_0.set_ylabel(r'$\bar H^t$',fontsize=sz1)
ax_0.tick_params(axis='both', labelsize=sz2)
ax_0.set_xlim(0,60)
ax_0.set_ylim(0.958,.983)

ax_1.set_ylabel(r'$\langle \bar H\rangle$',fontsize=sz1)
ax_1.tick_params(axis='both', labelsize=sz2)
ax_1.plot(.25,np.mean(mean_1),'C0o')
ax_1.plot(.75,np.mean(mean_2),'C1s')
ax_1.errorbar(.25,np.mean(mean_1),yerr=np.std(mean_1),color='C0',capsize=3)
ax_1.errorbar(.75,np.mean(mean_2),yerr=np.std(mean_2),color='C1',capsize=3)
ax_1.set_xlim(0,1)
ax_1.set_ylim(0.958,.983)
ax_1.set_xticks((.25,.75))
ax_1.set_xticklabels(['EC','EO'])

ax_0.text(61,0.980,'(a)',fontsize=sz1)
ax_1.text(1.05,0.980,'(b)',fontsize=sz1)

mean_1 = []
mean_2 = []

for i in range(len(X)):
    mean_1.append(np.mean(data_alpha_ec[:,i]))
    mean_2.append(np.mean(data_alpha_eo[:,i]))

mean_1 = np.array(mean_1)
mean_2 = np.array(mean_2)

ax_2.plot(X,mean_1,color='C0',alpha=0.85,label='EC')#,color='k',capsize=3)
ax_2.plot(X,mean_2,color='C1',alpha=0.85,label='EO')#,color='r',capsize=3)
ax_2.set_ylabel(r'$\bar H^t$',fontsize=sz1)
ax_2.set_xlabel(r'time (second)',fontsize=sz1)
ax_2.tick_params(axis='both', labelsize=sz2)
ax_2.set_xlim(0,60)
ax_2.set_ylim(0.925,.98)

ax_3.set_ylabel(r'$\langle \bar H\rangle$',fontsize=sz1)
ax_3.tick_params(axis='both', labelsize=sz2)
ax_3.plot(.25,np.mean(mean_1),'C0o')
ax_3.plot(.75,np.mean(mean_2),'C1s')
ax_3.errorbar(.25,np.mean(mean_1),yerr=np.std(mean_1),color='C0',capsize=3)
ax_3.errorbar(.75,np.mean(mean_2),yerr=np.std(mean_2),color='C1',capsize=3)
ax_3.set_xlim(0,1)
ax_3.set_ylim(0.925,.98)
ax_3.set_xticks((.25,0.75))
ax_3.set_xticklabels(['EC','EO'])

ax_2.text(61,0.973,'(c)',fontsize=sz1)
ax_3.text(1.05,0.973,'(d)',fontsize=sz1)

ax_2.legend(loc='upper right',fontsize=sz2-5,ncol=2)
fig.subplots_adjust(hspace=.25,wspace=.85,bottom=-0.4)
width = 28; height = 14;
fig.set_size_inches(width/2.54,height/2.54) #2.54 cm = 1 inches
plt.savefig('spatial_entropy.png', dpi=200,bbox_inches='tight')        

#---------------------------------------------------------------#

fig = plt.figure()
print('Generating figure 2')

gs = fig.add_gridspec(2,3)
ax_0 = fig.add_subplot(gs[0,:-1])
ax_1 = fig.add_subplot(gs[0,-1])

ax_2 = fig.add_subplot(gs[1,:-1])
ax_3 = fig.add_subplot(gs[1,-1])

s_data_raw_ec = np.load('shuffled_spatial_S_raw_ec.npy')
s_data_raw_eo = np.load('shuffled_spatial_S_raw_eo.npy')
s_data_alpha_ec = np.load('shuffled_spatial_S_alpha_ec.npy')
s_data_alpha_eo = np.load('shuffled_spatial_S_alpha_eo.npy')

mean_1 = []
mean_2 = []

for i in range(len(X)):
    mean_1.append(np.mean(s_data_raw_ec[:,i]))
    mean_2.append(np.mean(s_data_raw_eo[:,i]))

mean_1 = np.array(mean_1)
mean_2 = np.array(mean_2)

ax_0.plot(X,mean_1,color='C0',alpha=0.85,label='EC')#,color='k',capsize=3)
ax_0.plot(X,mean_2,color='C1',alpha=0.85,label='EO')#,color='r',capsize=3)
ax_0.set_ylabel(r'$\bar H^t$',fontsize=sz1)
ax_0.tick_params(axis='both', labelsize=sz2)
ax_0.set_xlim(0,60)
ax_0.set_ylim(0.978,.99)
ax_0.set_yticks((.98,0.99))

ax_1.set_ylabel(r'$\langle \bar H\rangle$',fontsize=sz1)
ax_1.tick_params(axis='both', labelsize=sz2)
ax_1.plot(.25,np.mean(mean_1),'C0o')
ax_1.plot(.75,np.mean(mean_2),'C1s')
ax_1.errorbar(.25,np.mean(mean_1),yerr=np.std(mean_1),color='C0',capsize=3)
ax_1.errorbar(.75,np.mean(mean_2),yerr=np.std(mean_2),color='C1',capsize=3)
ax_1.set_xlim(0,1)
ax_1.set_ylim(0.978,.99)
ax_1.set_xticks((.25,.75))
ax_1.set_xticklabels(['EC','EO'])
ax_1.set_yticks((.98,0.99))

ax_0.text(61,0.9885,'(a)',fontsize=sz1)
ax_1.text(1.05,0.9885,'(b)',fontsize=sz1)

mean_1 = []
mean_2 = []

for i in range(len(X)):
    mean_1.append(np.mean(s_data_alpha_ec[:,i]))
    mean_2.append(np.mean(s_data_alpha_eo[:,i]))

mean_1 = np.array(mean_1)
mean_2 = np.array(mean_2)

ax_2.plot(X,mean_1,color='C0',alpha=0.85,label='EC')#,color='k',capsize=3)
ax_2.plot(X,mean_2,color='C1',alpha=0.85,label='EO')#,color='r',capsize=3)
ax_2.set_ylabel(r'$\bar H^t$',fontsize=sz1)
ax_2.set_xlabel(r'time (second)',fontsize=sz1)
ax_2.tick_params(axis='both', labelsize=sz2)
ax_2.set_xlim(0,60)
ax_2.set_ylim(0.978,.99)
ax_2.set_yticks((.98,0.99))

ax_3.set_ylabel(r'$\langle \bar H\rangle$',fontsize=sz1)
ax_3.tick_params(axis='both', labelsize=sz2)
ax_3.plot(.25,np.mean(mean_1),'C0o')
ax_3.plot(.75,np.mean(mean_2),'C1s')
ax_3.errorbar(.25,np.mean(mean_1),yerr=np.std(mean_1),color='C0',capsize=3)
ax_3.errorbar(.75,np.mean(mean_2),yerr=np.std(mean_2),color='C1',capsize=3)
ax_3.set_xlim(0,1)
ax_3.set_ylim(0.978,.99)
ax_3.set_xticks((.25,0.75))
ax_3.set_xticklabels(['EC','EO'])
ax_3.set_yticks((.98,0.99))

ax_2.text(61,0.9885,'(c)',fontsize=sz1)
ax_3.text(1.05,0.9885,'(d)',fontsize=sz1)

ax_2.legend(loc='lower right',fontsize=sz2-5,ncol=2)
fig.subplots_adjust(hspace=.25,wspace=.85,bottom=-0.4)
width = 28; height = 14;
fig.set_size_inches(width/2.54,height/2.54) #2.54 cm = 1 inches
plt.savefig('shuffled_spatial_entropy.png', dpi=200,bbox_inches='tight')        

#---------------------------------------------------------------#

fig = plt.figure()
print('Generating figure 3')

gs = fig.add_gridspec(2,1)
ax_0 = fig.add_subplot(gs[0,0])
ax_1 = fig.add_subplot(gs[1,0])

mean_1 = []
mean_2 = []

for i in range(len(X)):
    mean_1.append(np.mean(data_raw_ec[:,i]))
    mean_2.append(np.mean(data_raw_eo[:,i]))

mean_1 = np.array(mean_1)
mean_2 = np.array(mean_2)

wd = 160
X = np.linspace(0,60,60)

Mean_1 = []
Mean_2 = []
Std_1 = []
Std_2 = []

for i in range(1,61):
    Mean_1.append(np.mean(mean_1[:i*wd]))
    Mean_2.append(np.mean(mean_2[:i*wd]))
    Std_1.append(np.std(mean_1[:i*wd]))
    Std_2.append(np.std(mean_2[:i*wd]))

Mean_1 = np.array(Mean_1)
Mean_2 = np.array(Mean_2)
Std_1 = np.array(Std_1)
Std_2 = np.array(Std_2)

ax_0.fill_between(X+1,Mean_1-Std_1,Mean_1+Std_1,color='C0',alpha=0.6)#,color='k',capsize=3)
ax_0.plot(X+1,Mean_1,color='C0',alpha=0.6,label='EC')#,color='k',capsize=3)

ax_0.fill_between(X+1,Mean_2-Std_2,Mean_2+Std_2,color='C1',alpha=0.6)#,color='r',capsize=3)
ax_0.plot(X+1,Mean_2,color='C1',alpha=0.6,label='EO')#,color='r',capsize=3)

mean_1 = []
mean_2 = []

for i in range(data_alpha_ec.shape[1]):
    mean_1.append(np.mean(data_alpha_ec[:,i]))
    mean_2.append(np.mean(data_alpha_eo[:,i]))

mean_1 = np.array(mean_1)
mean_2 = np.array(mean_2)

Mean_1 = []
Mean_2 = []
Std_1 = []
Std_2 = []

for i in range(1,61):
    Mean_1.append(np.mean(mean_1[:i*wd]))
    Mean_2.append(np.mean(mean_2[:i*wd]))
    Std_1.append(np.std(mean_1[:i*wd]))
    Std_2.append(np.std(mean_2[:i*wd]))

Mean_1 = np.array(Mean_1)
Mean_2 = np.array(Mean_2)
Std_1 = np.array(Std_1)
Std_2 = np.array(Std_2)

ax_1.fill_between(X+1,Mean_1-Std_1,Mean_1+Std_1,color='C0',alpha=0.6)#,color='k',capsize=3)
ax_1.plot(X+1,Mean_1,color='C0',alpha=0.8,label='EC')#,color='k',capsize=3)

ax_1.fill_between(X+1,Mean_2-Std_2,Mean_2+Std_2,color='C1',alpha=0.6)#,color='r',capsize=3)
ax_1.plot(X+1,Mean_2,color='C1',alpha=0.8,label='EO')#,color='r',capsize=3)

ax_0.set_ylabel(r'$\langle \bar H\rangle$',fontsize=sz1)
ax_1.set_ylabel(r'$\langle \bar H\rangle$',fontsize=sz1)

ax_1.set_xlabel(r'Analyzed time (second)',fontsize=sz1)
ax_0.tick_params(axis='both', labelsize=sz2)
ax_1.tick_params(axis='both', labelsize=sz2)

ax_0.set_xlim(0,60)
ax_1.set_xlim(0,60)

ax_0.set_ylim(0.965,.98)
ax_1.set_ylim(0.935,.975)

ax_0.text(61,0.978,'(a)',fontsize=sz1)
ax_1.text(61,0.970,'(b)',fontsize=sz1)

ax_1.legend(loc='upper right',fontsize=sz2-5,ncol=2)
fig.subplots_adjust(hspace=.25,wspace=.85,bottom=-0.4)
width = 28; height = 14;
fig.set_size_inches(width/2.54,height/2.54) #2.54 cm = 1 inches
plt.savefig('spatial_online.png', dpi=200,bbox_inches='tight')        

#---------------------------------------------------------------#