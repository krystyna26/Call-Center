class Call(object):
    def __init__(self, ID, callerName, callerPhone, time, reason):
        self.ID = ID
        self.callerName = callerName
        self.callerPhone = callerPhone
        self.time = time
        self.reason = reason

    def display(self):
        print "ID:",self.ID
        print "Caller name:", self.callerName
        print "Phone number:", self.callerPhone
        print "Time of call:", self.time
        print "Reason for call:", self.reason

class CallCenter(object):
    def __init__(self): # 'super(ChildClassName, self).parent_method()'.  
        self.callList = []
        self.queueSize = len(self.callList)

    def add(self,call): # adds a new call to the end of the call list
        self.callList.append(call)
        self.queueSize = len(self.callList)
        print "Added: {} to the end of the list".format(call.callerName)
        return self

    def remove(self, call): # removes the call from the beginning of the list (index 0).
        self.callList.remove(call)
        self.queueSize = len(self.callList)
        print "{} removed from the list".format(call.callerName)
        return self

    def info(self): # prints the name and phone number for each call in the queue as well as the length of the queue.
        print "Length of the queue: {} clients".format(self.queueSize)
        for item in self.callList:
            print item.callerName, item.callerPhone
        return self

caller1 = Call("H123oD", "John", "123.456.7890",2.30,"how to make cheesecake without the cheese?")
caller1.display()
print "\n"
caller2 = Call("BHi102", "Dana", "987.987.9876", 5.00,"what's the day today?")
caller2.display()

newCall = CallCenter()
print "\n"
newCall.add(caller1)
print "\n"
newCall.add(caller2)
print "\n"
newCall.remove(caller1)
print ""
newCall.info()