import FWCore.ParameterSet.Config as cms

CastorClusterRecoCustomKt = cms.EDProducer('CastorClusterProducer',
	inputtowers = cms.untracked.string("CastorTowerReco"),
	basicjets = cms.untracked.string(""),
	KtAlgo = cms.untracked.bool(True),
	ClusterAlgo = cms.untracked.bool(False),
	KtRecombination = cms.untracked.uint32(2),
	KtrParameter = cms.untracked.double(1.) )

CastorClusterRecoKt = cms.EDProducer('CastorClusterProducer',
	inputtowers = cms.untracked.string(""),
	basicjets = cms.untracked.string("CastorFastjetRecoKt"))

CastorClusterRecoSISCone = cms.EDProducer('CastorClusterProducer',
	inputtowers = cms.untracked.string(""),
	basicjets = cms.untracked.string("CastorFastjetRecoSISCone")) 
	

