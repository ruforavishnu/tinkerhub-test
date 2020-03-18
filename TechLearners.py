class TechLearnersAndMentors

	category = ""
	availableTime = 90;
	currentStacks = []


	def addStacks(expertise):
		currentStacks.append(expertise)

	def setMentorOrLearner(isLearnerOrMentor):
		category = isLearnerOrMentor
	def setAvailableTime():
		if(typeOfTechLearnerAndMentor == "mentor"):
			availableTime = 90



	def getMentor(reqdStack, availableTime ):
		#content
		for stack in currentStacks:
			if stack == reqdStack:
				if availableTime > 0:
					return self
					break
		return null







