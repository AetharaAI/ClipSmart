'use client';

import { motion } from 'framer-motion';
import { Upload, Brain, Scissors, Download, ArrowRight } from 'lucide-react';

const steps = [
  {
    number: '01',
    icon: Upload,
    title: 'Upload Your Video',
    description: 'Drag and drop your long-form content or paste a YouTube URL. Supports all major video formats.',
    color: 'from-neon-500 to-neon-600'
  },
  {
    number: '02',
    icon: Brain,
    title: 'AI Analysis',
    description: 'MiniMax-M2 analyzes attention patterns, engagement signals, and viral potential across your entire video.',
    color: 'from-purple-500 to-pink-600'
  },
  {
    number: '03',
    icon: Scissors,
    title: 'Generate Splices',
    description: 'Choose Semantic, Eclectic, or Trending mode. AI selects and combines the best clips into split-screen shorts.',
    color: 'from-blue-500 to-cyan-600'
  },
  {
    number: '04',
    icon: Download,
    title: 'Export & Share',
    description: 'Download platform-optimized videos with auto-generated captions and hashtags. Ready to go viral!',
    color: 'from-green-500 to-emerald-600'
  }
];

export function HowItWorksSection() {
  return (
    <section className="relative py-24 px-4 bg-ethereal-950">
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
            From Upload to <span className="text-neon-400">Viral</span> in Minutes
          </h2>
          <p className="text-xl text-ethereal-300 max-w-3xl mx-auto">
            Four simple steps to transform your content into engaging social media shorts
          </p>
        </motion.div>

        {/* Steps */}
        <div className="relative">
          {/* Connection Line */}
          <div className="hidden lg:block absolute top-1/2 left-0 right-0 h-0.5 bg-gradient-to-r from-neon-500/20 via-purple-500/20 to-green-500/20 -translate-y-1/2" />

          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8 relative">
            {steps.map((step, index) => (
              <motion.div
                key={step.number}
                initial={{ opacity: 0, y: 30 }}
                whileInView={{ opacity: 1, y: 0 }}
                viewport={{ once: true }}
                transition={{ duration: 0.5, delay: index * 0.15 }}
                className="relative"
              >
                {/* Step Card */}
                <div className="relative group">
                  {/* Number Badge */}
                  <div className={`absolute -top-6 -right-4 w-16 h-16 rounded-2xl bg-gradient-to-br ${step.color} flex items-center justify-center font-bold text-white text-lg shadow-lg z-10 group-hover:scale-110 transition-transform duration-300`}>
                    {step.number}
                  </div>

                  <div className="p-8 rounded-2xl bg-ethereal-800/50 backdrop-blur-sm border border-ethereal-700 hover:border-neon-500/50 transition-all duration-300 h-full">
                    {/* Icon */}
                    <div className={`w-16 h-16 rounded-xl bg-gradient-to-br ${step.color} flex items-center justify-center mb-6`}>
                      <step.icon className="w-8 h-8 text-white" />
                    </div>

                    {/* Content */}
                    <h3 className="text-2xl font-bold text-white mb-3">
                      {step.title}
                    </h3>
                    <p className="text-ethereal-300 leading-relaxed">
                      {step.description}
                    </p>
                  </div>
                </div>

                {/* Arrow (desktop only) */}
                {index < steps.length - 1 && (
                  <div className="hidden lg:flex absolute top-1/2 -right-4 transform -translate-y-1/2 z-20">
                    <ArrowRight className="w-6 h-6 text-neon-400" />
                  </div>
                )}
              </motion.div>
            ))}
          </div>
        </div>

        {/* Bottom Stats */}
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          transition={{ duration: 0.6, delay: 0.6 }}
          className="mt-20 grid grid-cols-1 md:grid-cols-3 gap-8 max-w-4xl mx-auto"
        >
          {[
            { value: '< 5 min', label: 'Average Processing Time' },
            { value: '90%', label: 'Time Saved vs Manual' },
            { value: '3x', label: 'Engagement Increase' }
          ].map((stat, index) => (
            <div key={index} className="text-center">
              <div className="text-4xl font-bold text-neon-400 mb-2">
                {stat.value}
              </div>
              <div className="text-ethereal-300">
                {stat.label}
              </div>
            </div>
          ))}
        </motion.div>
      </div>
    </section>
  );
}
