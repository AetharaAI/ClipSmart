'use client';

import { motion } from 'framer-motion';
import { Check, Zap, Crown, Building2 } from 'lucide-react';
import { useState } from 'react';

const plans = [
  {
    name: 'Free',
    icon: Zap,
    price: '0',
    period: 'forever',
    description: 'Perfect for trying out ClipSmart',
    features: [
      '10 videos per month',
      'AI-powered clip extraction',
      'Basic splice generation',
      '720p exports',
      'Standard processing',
      'Community support'
    ],
    cta: 'Get Started',
    popular: false,
    gradient: 'from-ethereal-600 to-ethereal-700'
  },
  {
    name: 'Pro',
    icon: Crown,
    price: '29',
    period: 'month',
    description: 'For serious content creators',
    features: [
      '100 videos per month',
      'Advanced AI analysis',
      'All 3 splice modes',
      '1080p & 4K exports',
      'Priority processing',
      'Custom watermarks',
      'Platform optimization',
      'Analytics dashboard',
      'Priority support'
    ],
    cta: 'Start Pro Trial',
    popular: true,
    gradient: 'from-neon-500 to-purple-600'
  },
  {
    name: 'Enterprise',
    icon: Building2,
    price: 'Custom',
    period: null,
    description: 'For teams and agencies',
    features: [
      'Unlimited videos',
      'White-label exports',
      'Team collaboration',
      'API access',
      'Custom AI training',
      'Dedicated account manager',
      'SLA guarantee',
      'Advanced analytics',
      '24/7 premium support'
    ],
    cta: 'Contact Sales',
    popular: false,
    gradient: 'from-purple-600 to-pink-600'
  }
];

export function PricingSection() {
  const [annual, setAnnual] = useState(false);

  return (
    <section id="pricing" className="relative py-24 px-4 bg-gradient-to-b from-ethereal-950 to-ethereal-900">
      <div className="max-w-7xl mx-auto">
        {/* Header */}
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          transition={{ duration: 0.6 }}
          className="text-center mb-12"
        >
          <h2 className="text-4xl md:text-5xl font-bold text-white mb-4">
            Simple, Transparent <span className="text-neon-400">Pricing</span>
          </h2>
          <p className="text-xl text-ethereal-300 max-w-3xl mx-auto mb-8">
            Start free, upgrade when you need more power
          </p>

          {/* Billing Toggle */}
          <div className="inline-flex items-center gap-4 p-1 bg-ethereal-800/50 rounded-full">
            <button
              onClick={() => setAnnual(false)}
              className={`px-6 py-2 rounded-full font-medium transition-all ${
                !annual
                  ? 'bg-neon-500 text-white shadow-lg'
                  : 'text-ethereal-300 hover:text-white'
              }`}
            >
              Monthly
            </button>
            <button
              onClick={() => setAnnual(true)}
              className={`px-6 py-2 rounded-full font-medium transition-all ${
                annual
                  ? 'bg-neon-500 text-white shadow-lg'
                  : 'text-ethereal-300 hover:text-white'
              }`}
            >
              Annual
              <span className="ml-2 text-xs bg-green-500 text-white px-2 py-0.5 rounded-full">
                Save 20%
              </span>
            </button>
          </div>
        </motion.div>

        {/* Plans Grid */}
        <div className="grid grid-cols-1 md:grid-cols-3 gap-8 max-w-6xl mx-auto">
          {plans.map((plan, index) => (
            <motion.div
              key={plan.name}
              initial={{ opacity: 0, y: 30 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true }}
              transition={{ duration: 0.5, delay: index * 0.1 }}
              className={`relative ${plan.popular ? 'md:-mt-4' : ''}`}
            >
              {/* Popular Badge */}
              {plan.popular && (
                <div className="absolute -top-4 left-1/2 transform -translate-x-1/2 z-10">
                  <div className="bg-gradient-to-r from-neon-500 to-purple-600 text-white px-4 py-1 rounded-full text-sm font-bold shadow-lg">
                    Most Popular
                  </div>
                </div>
              )}

              <div
                className={`h-full p-8 rounded-2xl border-2 transition-all duration-300 ${
                  plan.popular
                    ? 'border-neon-500 bg-ethereal-800/80 shadow-2xl shadow-neon-500/20 scale-105'
                    : 'border-ethereal-700 bg-ethereal-800/50 hover:border-neon-500/50'
                }`}
              >
                {/* Icon */}
                <div className={`w-14 h-14 rounded-xl bg-gradient-to-br ${plan.gradient} flex items-center justify-center mb-4`}>
                  <plan.icon className="w-7 h-7 text-white" />
                </div>

                {/* Plan Name */}
                <h3 className="text-2xl font-bold text-white mb-2">
                  {plan.name}
                </h3>
                <p className="text-ethereal-300 text-sm mb-6">
                  {plan.description}
                </p>

                {/* Price */}
                <div className="mb-6">
                  {plan.price === 'Custom' ? (
                    <div className="text-4xl font-bold text-white">
                      Custom
                    </div>
                  ) : (
                    <div className="flex items-baseline">
                      <span className="text-5xl font-bold text-white">
                        ${annual && plan.price !== '0' ? Math.round(Number(plan.price) * 0.8) : plan.price}
                      </span>
                      {plan.period && (
                        <span className="text-ethereal-300 ml-2">
                          /{plan.period}
                        </span>
                      )}
                    </div>
                  )}
                </div>

                {/* Features */}
                <ul className="space-y-3 mb-8">
                  {plan.features.map((feature, i) => (
                    <li key={i} className="flex items-start gap-3">
                      <Check className="w-5 h-5 text-neon-400 flex-shrink-0 mt-0.5" />
                      <span className="text-ethereal-200 text-sm">
                        {feature}
                      </span>
                    </li>
                  ))}
                </ul>

                {/* CTA Button */}
                <button
                  className={`w-full py-3 rounded-lg font-bold transition-all duration-300 ${
                    plan.popular
                      ? 'bg-gradient-to-r from-neon-500 to-purple-600 text-white hover:shadow-lg hover:shadow-neon-500/50'
                      : 'bg-ethereal-700 text-white hover:bg-ethereal-600'
                  }`}
                >
                  {plan.cta}
                </button>
              </div>
            </motion.div>
          ))}
        </div>

        {/* Money Back Guarantee */}
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          transition={{ duration: 0.6, delay: 0.3 }}
          className="text-center mt-12"
        >
          <p className="text-ethereal-300">
            All plans include a <span className="text-neon-400 font-bold">14-day money-back guarantee</span>
          </p>
        </motion.div>
      </div>
    </section>
  );
}
