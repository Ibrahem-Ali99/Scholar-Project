import React, { useRef, useEffect, useState } from 'react';
import Header from '../../components/Header/Header';
import MainBanner from '../../components/MainBanner/MainBanner';
import FeatureOffering from '../../components/FeatureOffering/FeatureOffering';

function StudentDashboard() {
  const headerRef = useRef(null);
  const [headerHeight, setHeaderHeight] = useState(0);

  useEffect(() => {
    const updateHeaderHeight = () => {
      if (headerRef.current) {
        setHeaderHeight(headerRef.current.offsetHeight);
      }
    };

    // Update height initially
    updateHeaderHeight();

    // Use ResizeObserver to monitor size changes
    const resizeObserver = new ResizeObserver(updateHeaderHeight);
    if (headerRef.current) {
      resizeObserver.observe(headerRef.current);
    }

    return () => {
      if (headerRef.current) {
        resizeObserver.unobserve(headerRef.current);
      }
    };
  }, []);

  return (
    <div className="student-dashboard">
      <Header ref={headerRef} />
      <MainBanner headerHeight={headerHeight} />
      <FeatureOffering />
    </div>
  );
}

export default StudentDashboard;
