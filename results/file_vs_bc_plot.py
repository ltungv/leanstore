import pandas as pd
import matplotlib.pyplot as plt


bc_log_bm = pd.read_csv('BC_bm.csv')  #buffer manager
bc_log_cpu = pd.read_csv('BC_cpu.csv')
bc_log_cr = pd.read_csv('BC_cr.csv')  #crash recovery ???  commit rate ??    gct Garbage Collection Time ?
bc_log_dt = pd.read_csv('BC_dt.csv')
bc_log_latency = pd.read_csv('BC_latency.csv')



file_log_bm = pd.read_csv('File_bm.csv')
file_log_cpu = pd.read_csv('File_cpu.csv')
file_log_cr = pd.read_csv('File_cr.csv')
file_log_dt = pd.read_csv('File_dt.csv')
file_log_latency = pd.read_csv('File_latency.csv')


# Create plots
fig, axs = plt.subplots(4, 2, figsize=(15, 15))
fig.suptitle('TPC-C Comparison: Bookkeeper vs File')

# Plot 1: consumed_pages
axs[0, 0].plot(bc_log_bm['t'], bc_log_bm['consumed_pages'], label='Bookkeeper',color='blue')
axs[0, 0].plot(file_log_bm['t'], file_log_bm['consumed_pages'], label='File', color='red')
axs[0, 0].set_title('consumed_pages over Time')
axs[0, 0].set_xlabel('Time')
axs[0, 0].set_ylabel('consumed_pages')
axs[0, 0].legend()

# Plot 2: CPU Usage over time
axs[0, 1].plot(bc_log_cpu['t'], bc_log_cpu['CPU'], label='Bookkeeper')
axs[0, 1].plot(file_log_cpu['t'], file_log_cpu['CPU'], label='File')
axs[0, 1].set_title('CPU Usage over Time')
axs[0, 1].set_xlabel('Time')
axs[0, 1].set_ylabel('CPU Usage')
axs[0, 1].legend()

# Plot 3: Abort% over time
axs[1, 0].plot(bc_log_cr['t'], bc_log_cr['tx_abort'], label='Bookkeeper')
axs[1, 0].plot(file_log_cr['t'], file_log_cr['tx_abort'], label='File')
axs[1, 0].set_title('Abort% over Time')
axs[1, 0].set_xlabel('Time')
axs[1, 0].set_ylabel('Abort Rate')
axs[1, 0].legend()

# Plot 4: GHz over time
axs[1, 1].plot(bc_log_cpu['t'], bc_log_cpu['GHz'], label='Bookkeeper')
axs[1, 1].plot(file_log_cpu['t'], file_log_cpu['GHz'], label='File')
axs[1, 1].set_title('Clock Speed (GHz) over Time')
axs[1, 1].set_xlabel('Time')
axs[1, 1].set_ylabel('GHz')
axs[1, 1].legend()

# Plot 5/6 r/w
axs[2, 0].plot(bc_log_bm["t"], bc_log_bm['w_mib'], label='writing bc')
axs[2, 0].plot(file_log_bm["t"], file_log_bm['w_mib'], label='writing file')
axs[2, 0].set_title('Write MiB over Time')
axs[2, 0].set_xlabel('Time')
axs[2, 0].set_ylabel('MiB')
axs[2, 0].legend()

axs[2, 1].plot(bc_log_bm["t"], bc_log_bm['r_mib'], label='reading bc')
axs[2, 1].plot(file_log_bm["t"], file_log_bm['r_mib'], label='reading file')
axs[2, 1].set_title('Read MiB over Time')
axs[2, 1].set_xlabel('Time')
axs[2, 1].set_ylabel('MiB')
axs[2, 1].legend()

# Plot 7 Latency
axs[3, 0].plot(bc_log_bm["t"], bc_log_bm['r_mib'], label='reading bc')
axs[3, 0].plot(file_log_bm["t"], file_log_bm['r_mib'], label='reading file')
axs[3, 0].set_title('Read/Write MiB over Time')
axs[3, 0].set_xlabel('Time')
axs[3, 0].set_ylabel('MiB')
axs[3, 0].legend()

axs[3, 1].plot(bc_log_bm["t"], bc_log_bm['r_mib'], label='reading bc')
axs[3, 1].plot(file_log_bm["t"], file_log_bm['r_mib'], label='reading file')
axs[3, 1].set_title('Read/Write MiB over Time')
axs[3, 1].set_xlabel('Time')
axs[3, 1].set_ylabel('MiB')
axs[3, 1].legend()




plt.tight_layout()
plt.savefig("plt.png")