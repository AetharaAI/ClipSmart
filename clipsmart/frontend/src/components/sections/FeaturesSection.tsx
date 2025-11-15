'use client';

import { motion } from 'framer-motion';
import {
  Brain,
  Scissors,
  Sparkles,
  LayoutGrid,
  Zap,
  Target,
  TrendingUp,
  Wand2
} from 'lucide-react';

const features = [
  {
    icon: Brain,
    title: 'AI-Powered Analysis',
    description: 'MiniMax-M2 analyzes your videos to identify the most engaging moments with attention scoring and content understanding.',
    gradient: 'from-neon-500 to-neon-600'
  },
  {
    icon: Scissors,
    title: 'Smart Clip Extraction',
    description: 'Automatically extract viral-worthy clips based on engagement signals, sentiment analysis, and trending patterns.',
    gradient: 'from-ethereal-500 to-ethereal-600'
  },
  {
    icon: LayoutGrid,
    title: 'Split-Screen Magic',
    description: 'Create stunning split-screen compositions that combine your best clips into attention-grabbing shorts.',
    gradient: 'from-purple-500 to-pink-600'
  },
  {
    icon: Sparkles,
    title: '3 Generation Modes',
    description: 'Semantic (thematic), Eclectic (variety), or Trending (viral potential) - choose your creative direction.',
    gradient: 'from-blue-500 to-cyan-600'
  },
  {
    icon: Target,
    title: 'Platform Optimization',
    description: 'Export perfectly formatted videos for TikTok, YouTube Shorts, and Instagram Reels with one click.',
    gradient: 'from-orange-500 to-red-600'
  },
  {
    icon: Zap,
    title: 'Lightning Fast',
    description: 'Process hours of footage in minutes. AI-powered workflows deliver professional results at unprecedented speed.',
    gradient: 'from-yellow-500 to-orange-600'
  },
  {
    icon: TrendingUp,
    title: 'Virality Scoring',
    description: 'Each clip gets engagement, attention, and virality scores to help you pick winners every time.',
    gradient: 'from-green-500 to-emerald-600'
  },
  {
    icon: Wand2,
    title: 'Auto Captions & Tags',
    description: 'AI-generated captions, hashtags, and descriptions tailored for each platform to maximize reach.',
    gradient: 'from-indigo-500 to-purple-600'
  }
];

export function FeaturesSection() {
  return (
    <section className="relative py-24 px-4 bg-gradient-to-b from-ethereal-900 to-ethereal-950">
      <div className="max-w-7xl mx-auto">
        {/* Header */}
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          transition={{ duration: 0.6 }}
          className="text-center mb-16"
        >
          <h2 className="text-4xl md:text-5xl font-bold text-white mb-4">
            Powered by <span className="text-neon-400">MiniMax-M2</span> AI
          </h2>
          <p className="text-xl text-ethereal-300 max-w-3xl mx-auto">
            Cut through the noise with AI that understands what makes content go viral
          </p>
        </motion.div>

        {/* Features Grid */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
          {features.map((feature, index) => (
            <motion.div
              key={feature.title}
              initial={{ opacity: 0, y: 20 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true }}
              transition={{ duration: 0.5, delay: index * 0.1 }}
              whileHover={{ y: -8, transition: { duration: 0.2 } }}
              className="group relative"
            >
              <div className="h-full p-6 rounded-2xl bg-ethereal-800/50 backdrop-blur-sm border border-ethereal-700 hover:border-neon-500/50 transition-all duration-300">
                {/* Icon */}
                <div className={`w-14 h-14 rounded-xl bg-gradient-to-br ${feature.gradient} flex items-center justify-center mb-4 group-hover:scale-110 transition-transform duration-300`}>
                  <feature.icon className="w-7 h-7 text-white" />
                </div>

                {/* Content */}
                <h3 className="text-xl font-bold text-white mb-2">
                  {feature.title}
                </h3>
                <p className="text-ethereal-300 text-sm leading-relaxed">
                  {feature.description}
                </p>

                {/* Hover effect */}
                <div className="absolute inset-0 rounded-2xl bg-gradient-to-br from-neon-500/5 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-300 pointer-events-none" />
              </div>
            </motion.div>
          ))}
        </div>

        {/* Bottom CTA */}
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          transition={{ duration: 0.6, delay: 0.4 }}
          className="text-center mt-16"
        >
          <p className="text-ethereal-300 text-lg">
            Ready to transform your content?{' '}
            <a href="#pricing" className="text-neon-400 hover:text-neon-300 underline transition-colors">
              Start for free
            </a>
          </p>
        </motion.div>
      </div>
    </section>
  );
}
