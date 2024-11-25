import React from 'react';
import './MainBanner.css';

function MainBanner({ headerHeight }) {
  return (
    <div className="main-banner" style={{ marginTop: `${headerHeight}px` }}>
      <div className="header-text">
        <h1 className="banner-title">Streamline Your Workflow with Scholar</h1>
        <p className="banner-description">
          Collaborate effectively with your team using an intuitive Scrum board
          designed to organize tasks, manage sprints, and track progress
          seamlessly. Empower your projects with clarity and efficiency.
        </p>
        <p className="banner-subtitle">Plan. Execute. Achieve.</p>
      </div>
    </div>
  );
}

export default MainBanner;
