import './ChatbotGuide.css'

function ChatbotGuide({ pageNumber = 1 }) {
  const guides = {
    1: {
      title: "Goal Garden Chatbot",
      steps: [
        "Ask about your goals and aspirations",
        "Track your progress with visual growth",
        "Get motivational insights",
        "Watch your plant grow with each interaction"
      ],
      tips: "The more you engage, the more your garden thrives!"
    },
    2: {
      title: "Progress Tracker Chatbot",
      steps: [
        "Discuss your daily achievements",
        "Set milestones and targets",
        "Review your growth journey",
        "Celebrate your successes"
      ],
      tips: "Every conversation helps your garden bloom!"
    }
  }

  const guide = guides[pageNumber] || guides[1]

  return (
    <div className="chatbot-guide">
      <div className="guide-header">
        <h3>How to Use</h3>
        <div className="guide-icon">📚</div>
      </div>
      
      <div className="guide-content">
        <h4 className="guide-title">{guide.title}</h4>
        
        <div className="guide-steps">
          {guide.steps.map((step, index) => (
            <div key={index} className="guide-step">
              <div className="step-number">{index + 1}</div>
              <div className="step-text">{step}</div>
            </div>
          ))}
        </div>
        
        <div className="guide-tip">
          <div className="tip-icon">💡</div>
          <p>{guide.tips}</p>
        </div>
      </div>
      
      <div className="guide-footer">
        <div className="decorative-line"></div>
        <span>Start chatting to see your garden grow!</span>
        <div className="decorative-line"></div>
      </div>
    </div>
  )
}

export default ChatbotGuide

