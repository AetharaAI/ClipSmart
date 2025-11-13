'use client';

import { useState, useEffect } from 'react';
import { motion } from 'framer-motion';
import Link from 'next/link';
import { 
  Play, 
  ArrowRight, 
  Sparkles, 
  Zap, 
  TrendingUp,
  Users,
  Clock,
  CheckCircle,
  Star
} from 'lucide-react';

interface HeroSectionProps {
  onGetStarted: () => void;
  onDemo: () => void;
}

export function HeroSection({ onGetStarted, onDemo }: HeroSectionProps) {
  const [currentStat, setCurrentStat] = useState(0);
  
  const stats = [
    { icon: Users, value: '10K+', label: 'Content Creators' },
    { icon: Zap, value: '2M+', label: 'Clips Generated' },
    { icon: TrendingUp, value: '300%', label: 'Engagement Boost' },
    { icon: Clock, value: '90%', label: 'Time Saved' },
  ];

  useEffect(() => {
    const interval = setInterval(() => {
      setCurrentStat((prev) => (prev + 1) % stats.length);
    }, 3000);
    
    return () => clearInterval(interval);
  }, [stats.length]);

  return (
    <section className="relative min-h-screen flex items-center justify-center overflow-hidden pt-16">
      {/* Animated Background */}
      <div className="absolute inset-0 z-0">
        <div className="absolute inset-0 bg-gradient-to-br from-ethereal-900 via-ethereal-800 to-neon-900 opacity-90" />
        <div className="absolute inset-0 bg-[url('data:image/svg+xml,%3Csvg width="60" height="60" viewBox="0 0 60 60" xmlns="http://www.w3.org/2000/svg"%3E%3Cg fill="none" fill-rule="evenodd"%3E%3Cg fill="%23ffffff" fill-opacity="0.05"%3E%3Ccircle cx="30" cy="30" r="1"/%3E%3C/g%3E%3C/g%3E%3C/svg%3E')] opacity-20" />
        
        {/* Floating particles */}
        {[...Array(20)].map((_, i) => (
          <motion.div
            key={i}
            className="absolute w-2 h-2 bg-neon-400 rounded-full opacity-60"
            style={{
              left: `${Math.random() * 100}%`,
              top: `${Math.random() * 100}%`,
            }}
            animate={{
              y: [0, -100, 0],
              opacity: [0.3, 1, 0.3],
            }}
            transition={{
              duration: 3 + Math.random() * 2,
              repeat: Infinity,
              delay: Math.random() * 2,
            }}
          />
        ))}
      </div>

      <div className="container mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
        <div className="grid lg:grid-cols-2 gap-12 items-center">
          {/* Left Column - Content */}
          <div className="text-center lg:text-left">
            {/* Badge */}
            <motion.div
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ delay: 0.2 }}
              className="inline-flex items-center space-x-2 bg-neon-600/20 border border-neon-500/30 rounded-full px-4 py-2 mb-6"
            >
              <Sparkles className="w-4 h-4 text-neon-400" />
              <span className="text-sm text-neon-300 font-medium">
                Powered by MiniMax-M2 AI
              </span>
            </motion.div>

            {/* Main Heading */}
            <motion.h1
              initial={{ opacity: 0, y: 30 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ delay: 0.3 }}
              className="text-4xl sm:text-5xl lg:text-6xl font-bold mb-6"
            >
              Transform Long Videos Into
              <span className="block bg-neon-gradient bg-clip-text text-transparent">
                Viral Shorts
              </span>
            </motion.h1>

            {/* Subheading */}
            <motion.p
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ delay: 0.4 }}
              className="text-xl text-ethereal-300 mb-8 max-w-2xl"
            >
              AI-powered content creation platform that analyzes your videos, extracts the best clips, 
              and creates engaging split-screen compositions optimized for TikTok, YouTube Shorts, and social media.
            </motion.p>

            {/* Feature Points */}
            <motion.div
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ delay: 0.5 }}
              className="flex flex-wrap justify-center lg:justify-start gap-4 mb-8"
            >
              {[
                'AI-Powered Clip Extraction',
                '3 Smart Splice Modes',
                'Social Media Optimized',
                'Auto-Generated Hooks'
              ].map((feature, index) => (
                <div key={feature} className="flex items-center space-x-2 text-sm text-ethereal-400">
                  <CheckCircle className="w-4 h-4 text-green-400" />
                  <span>{feature}</span>
                </div>
              ))}
            </motion.div>

            {/* CTA Buttons */}
            <motion.div
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ delay: 0.6 }}
              className="flex flex-col sm:flex-row gap-4 justify-center lg:justify-start mb-12"
            >
              <button
                onClick={onGetStarted}
                className="group relative bg-neon-gradient hover:shadow-neon text-white font-semibold py-4 px-8 rounded-xl transition-all duration-300 transform hover:scale-105"
              >
                <span className="flex items-center justify-center space-x-2">
                  <Play className="w-5 h-5" />
                  <span>Get Started Free</span>
                  <ArrowRight className="w-5 h-5 group-hover:translate-x-1 transition-transform" />
                </span>
              </button>
              
              <button
                onClick={onDemo}
                className="bg-transparent hover:bg-white/10 border-2 border-white/20 hover:border-white/40 text-white font-semibold py-4 px-8 rounded-xl transition-all duration-300"
              >
                Watch Demo
              </button>
            </motion.div>

            {/* Stats */}
            <motion.div
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ delay: 0.7 }}
              className="grid grid-cols-2 sm:grid-cols-4 gap-4"
            >
              {stats.map((stat, index) => {
                const Icon = stat.icon;
                const isActive = currentStat === index;
                
                return (
                  <motion.div
                    key={stat.label}
                    className={`text-center p-4 rounded-xl transition-all duration-300 ${
                      isActive 
                        ? 'bg-neon-600/20 border border-neon-500/30 scale-105' 
                        : 'bg-white/5 border border-white/10'
                    }`}
                    animate={isActive ? { scale: 1.05 } : { scale: 1 }}
                  >
                    <Icon className={`w-6 h-6 mx-auto mb-2 ${
                      isActive ? 'text-neon-400' : 'text-ethereal-400'
                    }`} />
                    <div className={`text-2xl font-bold ${
                      isActive ? 'text-white' : 'text-ethereal-300'
                    }`}>
                      {stat.value}
                    </div>
                    <div className="text-sm text-ethereal-400">
                      {stat.label}
                    </div>
                  </motion.div>
                );
              })}
            </motion.div>
          </div>

          {/* Right Column - Video Preview */}
          <motion.div
            initial={{ opacity: 0, x: 50 }}
            animate={{ opacity: 1, x: 0 }}
            transition={{ delay: 0.4, duration: 0.8 }}
            className="relative"
          >
            {/* Main Video Frame */}
            <div className="relative bg-black rounded-2xl overflow-hidden shadow-2xl transform rotate-3 hover:rotate-0 transition-transform duration-500">
              <div className="aspect-[9/16] bg-gradient-to-br from-neon-600/20 to-ethereal-800/20 flex items-center justify-center">
                <div className="text-center">
                  <motion.div
                    animate={{ scale: [1, 1.1, 1] }}
                    transition={{ repeat: Infinity, duration: 2 }}
                    className="w-20 h-20 bg-neon-gradient rounded-full flex items-center justify-center mx-auto mb-4"
                  >
                    <Play className="w-10 h-10 text-white" />
                  </motion.div>
                  <div className="text-white font-semibold mb-2">Video Preview</div>
                  <div className="text-ethereal-400 text-sm">AI processing in action</div>
                </div>
              </div>
              
              {/* Floating UI Elements */}
              <motion.div
                animate={{ y: [0, -10, 0] }}
                transition={{ repeat: Infinity, duration: 2 }}
                className="absolute top-4 right-4 bg-green-500 text-white px-3 py-1 rounded-full text-sm font-semibold"
              >
                AI Analyzing
              </motion.div>
              
              <motion.div
                animate={{ scale: [1, 1.2, 1] }}
                transition={{ repeat: Infinity, duration: 3 }}
                className="absolute bottom-4 left-4 bg-neon-600 text-white px-3 py-1 rounded-full text-sm font-semibold"
              >
                Score: 0.94
              </motion.div>
            </div>

            {/* Floating Elements */}
            <motion.div
              animate={{ 
                rotate: [0, 5, 0, -5, 0],
                y: [0, -20, 0]
              }}
              transition={{ 
                repeat: Infinity, 
                duration: 4,
                ease: "easeInOut"
              }}
              className="absolute -top-6 -left-6 bg-white/10 backdrop-blur-xl rounded-xl p-4 border border-white/20"
            >
              <div className="flex items-center space-x-2">
                <Star className="w-4 h-4 text-yellow-400" />
                <span className="text-white text-sm font-semibold">Viral Score: 94%</span>
              </div>
            </motion.div>

            <motion.div
              animate={{ 
                rotate: [0, -5, 0, 5, 0],
                y: [0, 20, 0]
              }}
              transition={{ 
                repeat: Infinity, 
                duration: 5,
                ease: "easeInOut"
              }}
              className="absolute -bottom-6 -right-6 bg-white/10 backdrop-blur-xl rounded-xl p-4 border border-white/20"
            >
              <div className="flex items-center space-x-2">
                <Zap className="w-4 h-4 text-blue-400" />
                <span className="text-white text-sm font-semibold">Processing Time: 23s</span>
              </div>
            </motion.div>
          </motion.div>
        </div>

        {/* Scroll Indicator */}
        <motion.div
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          transition={{ delay: 1 }}
          className="absolute bottom-8 left-1/2 transform -translate-x-1/2"
        >
          <motion.div
            animate={{ y: [0, 10, 0] }}
            transition={{ repeat: Infinity, duration: 2 }}
            className="w-6 h-10 border-2 border-white/30 rounded-full flex justify-center"
          >
            <motion.div
              animate={{ y: [0, 12, 0] }}
              transition={{ repeat: Infinity, duration: 2 }}
              className="w-1 h-3 bg-white/60 rounded-full mt-2"
            />
          </motion.div>
        </motion.div>
      </div>
    </section>
  );
}