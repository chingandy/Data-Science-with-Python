def successive_poisson(tau1, tau2, size=1):
    # Draw samples out of first exponential distribution: t1
    t1 = np.random.exponential(tau1, size = size)

    # Draw samples out of second exponential distribution: t2
    t2 = np.random.exponential(tau2, size = size)

    return t1 + t2

#---------------------------------------------------------------
# Draw samples of waiting times: waiting_times
waiting_times = successive_poisson(764, 715, 100000)

# Make the histogram
_ = plt.hist(waiting_times, bins = 100, normed = True, histtype ='step')


# Label axes
_= plt.xlabel('waiting time')
_ = plt.ylabel('PDF')

# Show the plot
plt.show()
