"""
Designing the offshore wind farm network topology using the spine-leaf network topology 
@Author: Agrippina W. Mwangi
@Created on: April 2024
"""

from mininet.topo import Topo

class MyTopo( Topo ):
    #Creating the WF1_AS1 Network Topology
    def build( self ):
        
        #Creating hosts
        '''
        Key: 
        1. LDAQ- Local Data acquisition, 
        2. MU - Merging Unit, 
        3. ECP - Edge Computing node, 
        4. vIED - virtual Intelligent Electronic Device
        '''
        
        ldaqwt1 = self.addHost('LDAQWT1')
        ldaqwt2 = self.addHost('LDAQWT2')
        ldaqwt3 = self.addHost('LDAQWT3')
        ldaqwt4 = self.addHost('LDAQWT4')
        ldaqwt5 = self.addHost('LDAQWT5')
        mu1 = self.addHost('MU1')
        mu2 = self.addHost('MU2')
        mu3 = self.addHost('MU3')
        mu4 = self.addHost('MU4')
        mu5 = self.addHost('MU5')
        vied1 = self.addHost('vIED1')
        vied2 = self.addHost('vIED2')
        vied3 = self.addHost('vIED3')
        vied4 = self.addHost('vIED4')
        vied5 = self.addHost('vIED5')
        ecp1 = self.addHost('ECP1')
        ecp2 = self.addHost('ECP2')
        ecp3 = self.addHost('ECP3')
        ecp4 = self.addHost('ECP4')
        ecp5 = self.addHost('ECP5')
        
        #Creating the WT Nacelle/Tower switches, Spine and Leaf Switches
        
        #Wind Turbine Nacelle/Tower Switches
        wt1_sw1 = self.addSwitch('WT1_SW1')    #Nacelle Switch
        wt1_sw2 = self.addSwitch('WT1_SW2')    #Tower Switch
        wt2_sw1 = self.addSwitch('WT2_SW1')
        wt2_sw2 = self.addSwitch('WT2_SW2')
        wt3_sw1 = self.addSwitch('WT3_SW1')
        wt3_sw2 = self.addSwitch('WT3_SW2')
        wt4_sw1 = self.addSwitch('WT4_SW1')
        wt4_sw2 = self.addSwitch('WT4_SW2')
        wt5_sw1 = self.addSwitch('WT5_SW1')
        wt5_sw2 = self.addSwitch('WT5_SW2')
        
        #Spine Switches (sp)
        sp1 = self.addSwitch('SP1')    #Spine Switch
        sp2 = self.addSwitch('SP2')
        sp3 = self.addSwitch('SP3')
        
        #Leaf Switches (fs)
        fs1 = self.addSwitch('fs1')
        fs2 = self.addSwitch('fs2')
        fs3 = self.addSwitch('fs3')
        fs4 = self.addSwitch('fs4')
        fs5 = self.addSwitch('fs5')
        fs6 = self.addSwitch('fs6')
        fs7 = self.addSwitch('fs7')
        fs8 = self.addSwitch('fs8')
        fs9 = self.addSwitch('fs9')
        fs10 = self.addSwitch('fs10')
        fs11 = self.addSwitch('fs11')
        fs12 = self.addSwitch('fs12')
        fs13 = self.addSwitch('fs13')
        fs14 = self.addSwitch('fs14')
        fs15 = self.addSwitch('fs15')
        fs16 = self.addSwitch('fs16')
            
        #Linking the devices  
        #LDAQ connects to the WT Access Network
        self.addLink(ldaqwt1,wt1_sw1)  
        self.addLink(ldaqwt2,wt2_sw1)
        self.addLink(ldaqwt3,wt3_sw1)
        self.addLink(ldaqwt4,wt4_sw1)
        self.addLink(ldaqwt5,wt5_sw1)
        #Nacelle switch connects to the tower switch
        self.addLink(wt1_sw1,wt1_sw2)   
        self.addLink(wt2_sw1,wt2_sw2)
        self.addLink(wt3_sw1,wt3_sw2)
        self.addLink(wt4_sw1,wt4_sw2)
        self.addLink(wt5_sw1,wt5_sw2)
        # WT Tower Switch connects to the spline switches (All of them for redundancy)
        self.addLink(wt1_sw2,sp1)      
        self.addLink(wt1_sw2,sp2)
        self.addLink(wt1_sw2,sp3)
        self.addLink(wt2_sw2,sp1)
        self.addLink(wt2_sw2,sp2)
        self.addLink(wt2_sw2,sp3)
        self.addLink(wt3_sw2,sp1)
        self.addLink(wt3_sw2,sp2)
        self.addLink(wt3_sw2,sp3)
        self.addLink(wt4_sw2,sp1)
        self.addLink(wt4_sw2,sp2)
        self.addLink(wt4_sw2,sp3)
        self.addLink(wt5_sw2,sp1)
        self.addLink(wt5_sw2,sp2)
        self.addLink(wt5_sw2,sp3)
        #creating a spine network sp1,sp2,sp3
        self.addLink(sp1,sp2)           
        self.addLink(sp1,sp3)
        self.addLink(sp2,sp3)
        #creating a mesh link between the spine and the distribution leaf switches
        self.addLink(sp1,fs1)        
        self.addLink(sp1,fs2)
        self.addLink(sp1,fs3)
        self.addLink(sp1,fs4)
        self.addLink(sp2,fs1)
        self.addLink(sp2,fs2)
        self.addLink(sp2,fs3)
        self.addLink(sp2,fs4)
        self.addLink(sp3,fs1)
        self.addLink(sp3,fs2)
        self.addLink(sp3,fs3)
        self.addLink(sp3,fs4)
        #Creating the leaf network with maximum redundancy
        self.addLink(fs1,fs2)
        self.addLink(fs2,fs3)
        self.addLink(fs3,fs4)
        self.addLink(fs4,fs5)
        self.addLink(fs5,fs6)
        self.addLink(fs6,fs7)
        self.addLink(fs7,fs8)
        self.addLink(fs9,fs10)
        self.addLink(fs10,fs11)
        self.addLink(fs11,fs12)
        self.addLink(fs12,fs13)
        self.addLink(fs13,fs14)
        self.addLink(fs15,fs16)
        self.addLink(fs1,fs16)
        self.addLink(fs16,fs2)
        self.addLink(fs15,fs5)
        self.addLink(fs14,fs4)
        self.addLink(fs13,fs3)
        self.addLink(fs12,fs6)
        self.addLink(fs11,fs7)
        self.addLink(fs10,fs4)
        #Linking MU nodes with the leaf switches
        self.addLink(fs5,mu1)
        self.addLink(fs6,mu2)
        self.addLink(fs7,mu3)
        self.addLink(fs8,mu4)
        self.addLink(fs9,mu5)
        self.addLink(fs10,vied1)
        self.addLink(fs11,vied2)
        self.addLink(fs12,vied3)
        self.addLink(fs13,vied4)
        self.addLink(fs14,vied5)
        self.addLink(fs10,ecp1)
        self.addLink(fs11,ecp2)
        self.addLink(fs12,ecp3)
        self.addLink(fs13,ecp4)
        self.addLink(fs14,ecp5)
        
topos = { 'mytopo': (lambda: MyTopo() )}
