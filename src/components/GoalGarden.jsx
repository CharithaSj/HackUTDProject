import { useEffect, useState } from 'react'
import { motion } from 'framer-motion'
import './GoalGarden.css'

function GoalGarden({ growth = 0, pageNumber = 1 }) {
  const [plantHeight, setPlantHeight] = useState(20)
  const [stage, setStage] = useState('sprout') // 'sprout', 'plant', 'flowering'
  
  useEffect(() => {
    // Update plant based on growth metric
    const targetHeight = Math.min(20 + growth * 2, 120)
    setPlantHeight(targetHeight)
    
    // Determine growth stage
    if (growth < 30) {
      setStage('sprout')
    } else if (growth < 100) {
      setStage('plant')
    } else {
      setStage('flowering')
    }
  }, [growth])

  return (
    <div className="goal-garden">
      <div className="garden-header">
        <h4>Goal Garden</h4>
        <div className="growth-indicator">
          <span className="growth-value">{Math.min(Math.floor(growth), 100)}%</span>
        </div>
      </div>
      
      <div className="garden-pot">
        <div className="pot-top"></div>
        <div className="pot-body"></div>
      </div>
      
      <motion.div 
        className="plant-container"
        animate={{ height: `${Math.min(plantHeight, 120)}px` }}
        transition={{ duration: 1, ease: "easeOut" }}
      >
        {/* Sprout Stage (0-30%) */}
        {stage === 'sprout' && (
          <motion.div 
            className="sprout-stage"
            initial={{ scale: 0.8, opacity: 0 }}
            animate={{ scale: 1, opacity: 1 }}
            transition={{ duration: 0.5 }}
          >
            <div className="sprout-stem"></div>
            <div className="sprout-leaf leaf-1"></div>
            <div className="sprout-leaf leaf-2"></div>
          </motion.div>
        )}
        
        {/* Plant Stage (30-100%) */}
        {stage === 'plant' && (
          <motion.div 
            className="plant-stage"
            initial={{ scale: 0.8, opacity: 0 }}
            animate={{ scale: 1, opacity: 1 }}
            transition={{ duration: 0.5 }}
          >
            <motion.div 
              className="plant-stem"
              animate={{ height: `${Math.min(plantHeight * 0.8, 100)}px` }}
              transition={{ duration: 1, ease: "easeOut" }}
            />
            <div className="plant-leaf plant-leaf-1"></div>
            <div className="plant-leaf plant-leaf-2"></div>
            <div className="plant-leaf plant-leaf-3"></div>
            <div className="plant-leaf plant-leaf-4"></div>
            <div className="plant-leaf plant-leaf-5"></div>
          </motion.div>
        )}
        
        {/* Flowering Stage (100%) */}
        {stage === 'flowering' && (
          <motion.div 
            className="flowering-stage"
            initial={{ scale: 0.8, opacity: 0 }}
            animate={{ scale: 1, opacity: 1 }}
            transition={{ duration: 0.5 }}
          >
            <motion.div 
              className="plant-stem"
              animate={{ height: `${Math.min(plantHeight * 0.8, 100)}px` }}
              transition={{ duration: 1, ease: "easeOut" }}
            />
            <div className="plant-leaf plant-leaf-1"></div>
            <div className="plant-leaf plant-leaf-2"></div>
            <div className="plant-leaf plant-leaf-3"></div>
            <div className="plant-leaf plant-leaf-4"></div>
            <div className="plant-leaf plant-leaf-5"></div>
            <div className="plant-leaf plant-leaf-6"></div>
            {/* Flowers */}
            <motion.div 
              className="flower flower-1"
              animate={{ 
                rotate: [0, 5, -5, 0],
                scale: [1, 1.1, 1]
              }}
              transition={{ 
                duration: 3,
                repeat: Infinity,
                repeatType: "reverse"
              }}
            >
              <div className="flower-petal petal-1"></div>
              <div className="flower-petal petal-2"></div>
              <div className="flower-petal petal-3"></div>
              <div className="flower-petal petal-4"></div>
              <div className="flower-center"></div>
            </motion.div>
            <motion.div 
              className="flower flower-2"
              animate={{ 
                rotate: [0, -5, 5, 0],
                scale: [1, 1.1, 1]
              }}
              transition={{ 
                duration: 3,
                repeat: Infinity,
                repeatType: "reverse",
                delay: 0.5
              }}
            >
              <div className="flower-petal petal-1"></div>
              <div className="flower-petal petal-2"></div>
              <div className="flower-petal petal-3"></div>
              <div className="flower-petal petal-4"></div>
              <div className="flower-center"></div>
            </motion.div>
          </motion.div>
        )}
        
        {/* Growth sparkles */}
        {growth > 50 && (
          <motion.div
            className="growth-sparkle"
            animate={{
              scale: [1, 1.5, 1],
              opacity: [0.5, 1, 0.5],
            }}
            transition={{
              duration: 2,
              repeat: Infinity,
            }}
          >
            ✨
          </motion.div>
        )}
      </motion.div>
      
    </div>
  )
}

export default GoalGarden
