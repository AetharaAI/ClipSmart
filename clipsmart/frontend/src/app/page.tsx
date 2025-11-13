'use client';

import { useState } from 'react';
import { motion } from 'framer-motion';
import Link from 'next/link';
import { useAuthStore } from '@/lib/stores';
import { HeroSection } from '@/components/sections/HeroSection';
import { FeaturesSection } from '@/components/sections/FeaturesSection';
import { HowItWorksSection } from '@/components/sections/HowItWorksSection';
import { PricingSection } from '@/components/sections/PricingSection';
import { TestimonialsSection } from '@/components/sections/TestimonialsSection';
import { CTASection } from '@/components/sections/CTASection';
import { AuthModal } from '@/components/modals/AuthModal';
import { useUIStore } from '@/lib/stores';

export default function HomePage() {
  const { isAuthenticated } = useAuthStore();
  const { openModal, addNotification } = useUIStore();
  const [showAuthModal, setShowAuthModal] = useState(false);

  const handleGetStarted = () => {
    if (!isAuthenticated) {
      setShowAuthModal(true);
    }
  };

  const handleDemo = () => {
    addNotification({
      type: 'info',
      title: 'Demo Coming Soon',
      message: 'Interactive demo will be available in the next version!',
    });
  };

  return (
    <div className="overflow-hidden">
      {/* Hero Section */}
      <HeroSection onGetStarted={handleGetStarted} onDemo={handleDemo} />

      {/* Features Section */}
      <FeaturesSection />

      {/* How It Works Section */}
      <HowItWorksSection />

      {/* Pricing Section */}
      <PricingSection onGetStarted={handleGetStarted} />

      {/* Testimonials Section */}
      <TestimonialsSection />

      {/* CTA Section */}
      <CTASection onGetStarted={handleGetStarted} />

      {/* Auth Modal */}
      {showAuthModal && (
        <AuthModal
          isOpen={showAuthModal}
          onClose={() => setShowAuthModal(false)}
        />
      )}
    </div>
  );
}

// Static page generation optimization
export const dynamic = 'force-static';
export const revalidate = 3600; // Revalidate every hour